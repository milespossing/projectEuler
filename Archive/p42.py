# triangle numbers

from __future__ import division
import string
from MathPackage.StringOperations import Str2CharArr, LetterSum


def tri(length):
    out = []
    for i in range(0,length):
        out.append((i / 2) * (i + 1))
    return out

class p42:

    def __init__(self):
        self.triangles = tri(100)
        self.max = self.triangles[-1]
        self.length = 100

    def updateTriangles(self):
        self.length = self.length * 1.5
        self.triangles = tri(self.length)
        self.max = self.triangles[-1]

    def isTriangle(self,num):
        while num > self.max:
            self.updateTriangles()
        return num in self.triangles

with open('files\\p42.txt') as f:
    read = str(f.read())
    read = read.translate(string.maketrans('', ''), '"')
    all = read.split(',')
    print(all)

p = p42()

count = 0

for s in all:
    c = Str2CharArr(s)
    letterSum = LetterSum(c)
    if p.isTriangle(letterSum):
        count += 1
        print(s)
        print(count)

print(count)
