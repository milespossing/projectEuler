from __future__ import division
from sympy import isprime

def primeCheck(arr):
    count = 0
    for a in arr:
        if isprime(a):
            count += 1
    return count / len(arr)

sideLength = 2
primes = 0
comps = 1
first = 1

def check(p,c):
    if c == 0: return False
    if p == 0: return False
    if p / (p + c) > .1: return False
    return True

while not check(primes,comps):
    print"+--------------+"
    for i in range(1,5):
        val = first + i * sideLength
        print(val)
        if isprime(val): primes += 1
        else: comps += 1
    first = first + 4 * sideLength
    sideLength += 2
    print " "
    print("Side:")
    print(sideLength - 1)
    print(primes/(primes + comps))

print("answer")
print(sideLength - 1)
