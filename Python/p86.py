import numpy as np
import sympy as sp

class SquareChecker:
    def __init__(self, n=10000):
        self.squares = []
        self.val = 1
        self.extend(n)

    def extendOne(self):
        self.squares.append(self.val * self.val)
        self.val += 1

    def extendSquaresTo(self,n):
        while max(self.squares) < n:
            self.extendOne()

    def extend(self,n):
        for i in range(self.val,n):
            self.squares.append(i * i)
        self.val = n

    def isSquare(self,n):
        while (n > max(self.squares)):
            self.extendOne()
            print(f"Extended to: {self.val}")
        return n in self.squares

    def getPotentials(self,n):
        output = [self.checkPair(n,s) for s in self.squares if s <= (2 * n * n)]
        return sum(output)

    def checkPair(self,n,s):
        s = np.sqrt(s - n ** 2)
        if s % 1 == 0:
            return s
        else:
            return 0


def solve(n,checker):
    # getSquares(n)
    checker.extendSquaresTo(2 * (n ** 2))
    return checker.getPotentials(n)
    # s = n * n
    # for i in range(1,n + 1):
    #     for j in range(1,i + 1):
    #         if checker.isSquare(s + (i + j)**2):
    #             print("pass")
    #             output += 1
    # return output

squares = []

if __name__ == '__main__':
    solutions = 1975
    m = 99
    checker = SquareChecker()
    while solutions < 1000000:
        print(f"{m}: {solutions}")
        m += 1
        # p.factor(m)
        checker = SquareChecker()        solutions += solve(m,checker)
    print(m)
    print(solutions)
