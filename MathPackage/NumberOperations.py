from __future__ import division
import numpy
from collections import Counter

def Dec2Frac(val):
    val = val % 1
    num = 1
    den = 2
    current = num / den
    while current != val:
        if current > val:
            den += 1
        elif current < val:
            num += 1
        current = num / den
    return [num,den]

def Num2Dig(val):
    return [int(d) for d in str(val)]

def Dig2Num(dig):
    output = 0
    length = len(dig)
    for i in range(0,length):
        output += dig[-i -1] * (10 ** i)
    return output

def IndexOf(array, val):
    for i in range(0,len(array)):
        if (array[i] == val): return i
    return -1

def Factor(num):
    output = []
    for i in range(2,num + 1):
        if num % i == 0:
            output.append(i)
    return output

def panDigital(num):
    arr = Num2Dig(num)
    return panArray(arr)

def panArray(arr):
    c = Counter(arr)
    if c.most_common()[0][1] > 1: return False
    return True

def hasDuplicates(num):
    arr = Num2Dig(num)
    for i in range(0,len(arr)):
        current = arr[i]
        if current in arr[i + 1:]:
            return True
    return False

def isPermutation(numA, numB):
    arrA = Num2Dig(numA)
    arrB = Num2Dig(numB)
    for a in arrA:
        if arrB.count(a) != arrA.count(a):
            return False
    return True

def isPalindrome(num):
    numA = Num2Dig(num)
    i = 0
    j = len(numA) - 1
    while i < j:
        if numA[i] != numA[j]: return False
        i += 1
        j -= 1
    return True

def reverse(num):
    numA = Num2Dig(num)
    output = []
    for i in reversed(numA):
        output.append(i)
    return Dig2Num(output)

def combiner(left,right):
    rDigs = numpy.floor(numpy.log10(right)) + 1
    left *= 10 ** rDigs
    return int(left + right)

class fibonacci:

    def __init__(self):
        self.current = 1
        self.last = 1
        self.arr = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.arr) < 2:
            self.arr.append(1)
            return 1
        else:
            val = self.arr[-1] + self.arr[-2]
            self.arr.append(val)
            return val
