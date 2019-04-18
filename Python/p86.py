import numpy as np
import sympy as sp

class primeFactorChecker:
    def __init__(self):
        self.factors = dict()

    def factor(self,n):
        if n in self.factors: return
        f = sp.factorint(n)
        self.factors[n] = f

    def checkSquare(self,m,n):

        self.factor(n)
        self.factor(m)
        mf = self.factors[m]
        nf = self.factors[n]
        common = []
        mU = []
        nU = list(nf.keys())
        for key in mf:
            if key in nf:
                common.append(key)
                nU.remove(key)
            else: mU.append(key)
        # check all common factors are equal modulo
        for key in common:
            if mf[key] % 2 != nf[key] % 2:
                return False
        # check all unique factors are even
        for key in mU:
            if mf[key] % 2 != 0: return False
        for key in nU:
            if nf[key] % 2 != 0: return False
        return True

def router(l):
    return p.checkSquare(l[0] + l[1], l[2])

def solve(n):
    # getSquares(n)
    output = 0
    for i in range(1,n + 1):
        for j in range(1,i + 1):
            if router([n, i, j]):
                output += 1
    return output

p = primeFactorChecker()

if __name__ == '__main__':
    solutions = 1975
    m = 99
    while solutions < 1000000:
        print(f"{m}: {solutions}")
        m += 1
        p.factor(m)
        solutions += solve(m)
    print(m)
    print(solutions)