from Timer import timer
import numpy as np
# from decimal import *
# getcontext().prec = 12

class Pair:
    def __init__(self, base, power, index):
        self.logValue = None
        self.base = base
        self.power = power
        self.index = index

    def __str__(self):
        return f"{self.index}: {self.base}^{self.power}; {self.log()}"

    def __repr__(self):
        return str(self)

    def __lt__(self,other):
        return self.log() < other.log()

    def log(self):
        if self.logValue is not None:
            return self.logValue
        output = np.log(self.base)
        self.logValue = self.power * output
        return self.logValue

@timer
def main():
    file = open('files/p099.txt')
    lines = file.readlines()
    pairs = []
    index = -1
    secondIndex = -1
    biggest = None
    largest = 0
    second = 0
    for i in range(len(lines)):
        line = lines[i]
        line.replace('\n','')
        s = line.split(',')
        pair = Pair(int(s[0]), int(s[1]),i + 1)
        current = pair.log()
        pairs.append(pair)
        if current > largest:
            biggest = pair
            largest = current

    pairs.sort()
    for p in pairs:
        print(p)

    print(len(pairs))
    # print(reversed(pairs))
    # print(biggest)

if __name__ == '__main__':
    main()