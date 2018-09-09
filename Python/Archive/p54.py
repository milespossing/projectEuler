from itertools import groupby
from collections import Counter

class Card:
    def __init__(self, st):
        value = st[0]
        self.value = 0
        if value == 'T': self.value = 10
        elif value == 'J': self.value = 11
        elif value == 'Q': self.value = 12
        elif value == 'K': self.value = 13
        elif value == 'A': self.value = 14
        else: self.value = int(value)
        self.suit = st[1]

class Hand:
    def __init__(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def maxValue(self):
        return max(self.values())

    def suits(self):
        return map(lambda x: x.suit, self.cards)

    def values(self):
        return map(lambda x: x.value, self.cards)

    def score(self):
        if self.hasStraight() and self.hasFlush():
            return [8,self.maxValue()] # straight flush - could be royal
        c = self.cardCount()
        if 4 in c.values():
            v4 = c.values().index(4)
            v4 = c.keys()[v4]
            return [7, v4]
        if 2 in c.values() and 3 in c.values():
            v3 = c.values().index(3)
            v3 = c.keys()[v3]
            return [6, v3]
        if self.hasFlush():
            return [5,self.maxValue()]
        if self.hasStraight():
            return [4,self.maxValue()]
        if 3 in c.values():
            v3 = c.values().index(3)
            v3 = c.keys()[v3]
            return [3, v3]
        if 2 in c.values():
            count2 = 0
            for i in c.values():
                if i == 2: count2 += 1
            if count2 == 2:
                vals = []
                for i in range(0,len(c.values())):
                    if c.values()[i] == 2:
                        vals.append(c.keys()[i])
                return [2,max(vals)]
            else:
                v2 = c.values().index(2)
                v2 = c.keys()[v2]
                return [1, v2]
        return [0,self.maxValue()]

    def hasFlush(self):
        if len([len(list(group)) for key, group in groupby(self.suits())]) == 1: return True
        return False

    def hasStraight(self):
        s = sorted(self.values())
        for i in range(0,4):
            if s[i + 1] - s[i] != 1: return False
        return True

    def cardCount(self):
        return Counter(self.values())

output = 0

def parseLine(arr):
    hand1 = Hand()
    hand2 = Hand()
    for i in range(0,5):
        hand1.add(Card(arr[i]))
    for i in range(5,10):
        hand2.add(Card(arr[i]))
    h1S = hand1.score()
    h2S = hand2.score()
    if (h1S[0] > h2S[0]): return True
    elif (h1S[0] == h2S[0]):
        if h1S[1] > h2S[1]: return True
        elif h1S[1] == h2S[1]:
            return compare(hand1,hand2)
    return False

def compare(h1,h2):
    i = 0
    s1 = sorted(h1.values(), reverse=True)
    s2 = sorted(h2.values(), reverse=True)
    while (s1[i] == s2[i]):
        i += 1
    return s1[i] > s2[i]

def getCards(file):
    output = 0
    f = open(file,"r")
    for line in f.readlines():
        line = line.replace("\n","")
        test = parseLine(line.split(" "))
        if test: output += 1
    return output

print(getCards("files\\p54.txt"))
