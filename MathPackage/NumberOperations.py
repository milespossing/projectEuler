from __future__ import division
from numpy import sqrt

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
    for i in range(1,len(arr) + 1):
        count = 0
        for a in arr:
            if i == a:
                count += 1
        if count != 1:
            return False
    return True

def hasDuplicates(num):
    arr = Num2Dig(num)
    for i in range(0,len(arr)):
        current = arr[i]
        if current in arr[i + 1:]:
            return True
    return False