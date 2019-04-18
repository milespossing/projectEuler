from __future__ import division
from sympy import primefactors, isprime, sieve
from MathPackage.NumberOperations import isPermutation
from Timer import timer

def phi(n):
    out = 1
    for p in primefactors(n):
        out *= 1 - (1 / p)
    return int(n * out)

@timer
def run():
    c = 0
    # sieve.extend(10000000)
    n = 1
    m = 10000000
    ran = sieve.totientrange(0,m)
    candidates = []
    for i in sieve.totientrange(2,m):
        n += 1
        # print(n)
        if isPermutation(n,i):
            candidates.append([n,n/i])
        # print(f"count: {c}: {i}")
    print(len(candidates))
    out = min(candidates,key=lambda x:x[1])
    print(out)

    # print(len(sieve))
    # for p in sieve:
    #     print(p)
    # print(2)
    # max = 10000000
    # minRatio = 99999
    # n = 99999
    # for i in range(max, max-100000,-1):
    #     p = phi(i)
    #     if isPermutation(i,p):
    #         if i / p < minRatio:
    #             minRatio = i/p
    #             n = i
    #     print(i)
    # print("n: ", n)
    # print("phi(n): ", phi(n))
    # print("ratio: ", minRatio)


if __name__ == '__main__':
    run()
