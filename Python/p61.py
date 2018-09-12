from abc import abstractmethod
from .MathPackage.NumberOperations import Num2Dig


class entry:
    def __init__(self, n, fig):
        self.value = n
        self.possible = []
        self.type = fig

class Figurate:
    def __init__(self):
        self.values = []
        self.current = 0

    @property
    @abstractmethod
    def number(self):
        pass

    def iterate(self):
        self.current += 1
        self.values.append(entry(self.current, self.number))

    @abstractmethod
    def calc(self,n):
        pass

class Triangle(Figurate):
    def number(self):
        return 3

    def calc(self,n):
        return n * (n + 1) / 2

class Square(Figurate):
    def number(self):
        return 4

    def calc(self,n):
        return n ** 2

class Pentagon(Figurate):
    def number(self):
        return 5

    def calc(self,n):
        return n * ( 3 * n - 1) / 2

class Hexagon(Figurate):
    def number(self):
        return 6

    def calc(self,n):
        return n * ( 2 * n - 1)

class Septagon(Figurate):
    def number(self):
        return 7

    def calc(self,n):
        return n * (5 * n - 3) / 2

class Octogon(Figurate):
    def number(self):
        return 8

    def calc(self,n):
        return n * (3 * n - 2)

def test(left,right):
    lDigs = Num2Dig(left.value)
    rDigs = Num2Dig(right.value)
    if lDigs[-2] == rDigs[0] and lDigs[-1] == rDigs[1]:
        left.possible.append(right)

if __name__ == "__main__":

