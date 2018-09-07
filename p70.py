from __future__ import division
from sympy import primefactors, isprime
from MathPackage.NumberOperations import isPermutation
from Timer import timer

def phi(n):
    out = 1
    for p in primefactors(n):
        out *= 1 - (1 / p)
    return int(n * out)

@timer
def __init__():
    max = 10000000
    minRatio = 99999
    n = 99999
    for i in range(max, max-100000,-1):
        p = phi(i)
        if isPermutation(i,p):
            if i / p < minRatio:
                minRatio = i/p
                n = i
        print(i)
    print "n: ", n
    print "phi(n): ", phi(n)
    print "ratio: ", minRatio
