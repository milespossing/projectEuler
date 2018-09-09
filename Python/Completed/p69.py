from __future__ import division
from sympy import primefactors

def phi(n):
    out = 1
    for p in primefactors(n):
        out *= 1 - (1 / p)
    return n * out

def term(n):
    return n / phi(n)

t = 1000000
m = 2
for i in range(2,t + 1):
    if term(i) > term(m):
        m = i
    print i
print m

# Answer: 510510