from __future__ import division
import numpy
from collections import Counter
from fractions import Fraction

def Dec2Frac(val):
    return val.as_integer_ratio()
    # whole = val // 1
    # val = val % 1
    # if val == 0:
    #     return [whole,1]
    # num = 1
    # den = 2
    # current = num / den
    # while abs(current - val) > .00000000000000001:
    #     if current > val:
    #         den += 1
    #     elif current < val:
    #         num += 1
    #     current = num / den
    # return [whole * den + num,den]

def num2Dig(val):
    return [int(d) for d in str(val)]

def Dig2Num(dig):
    output = 0
    length = len(dig)
    for i in range(0,length):
        output += dig[-i -1] * (10 ** i)
    return output

def DigCount(num):
    return numpy.floor(numpy.log10(num)) + 1

def DigCountLong(num):
    return len([d for d in str(num)])

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
    arr = num2Dig(num)
    return panArray(arr)

def panArray(arr):
    c = Counter(arr)
    if c.most_common()[0][1] > 1: return False
    return True

def hasDuplicates(num):
    arr = num2Dig(num)
    for i in range(0,len(arr)):
        current = arr[i]
        if current in arr[i + 1:]:
            return True
    return False

def isPermutation(numA, numB):
    arrA = num2Dig(numA)
    arrB = num2Dig(numB)
    if len(arrA) != len(arrB): return False
    arrA.sort()
    arrB.sort()
    return arrA == arrB

def isPalindrome(num):
    numA = num2Dig(num)
    i = 0
    j = len(numA) - 1
    while i < j:
        if numA[i] != numA[j]: return False
        i += 1
        j -= 1
    return True

def reverse(num):
    numA = num2Dig(num)
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
