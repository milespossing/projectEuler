from abc import abstractmethod
from MathPackage.NumberOperations import Num2Dig


class entry:
    def __init__(self, n, sides):
        self.value = n
        self.possible = []
        self.sides = sides

    def __str__(self):
        return self.value + "; " + str(len(self.possible)) + " possible"


class Figurate:
    def __init__(self):
        self.values = []
        self.current = 0
        self.iterate()
        while self.values[-1].value < 10000:
            self.iterate()
            if self.values[0].value < 1000:
                self.values.remove(self.values[0])
        self.values.remove(self.values[-1])

    @property
    @abstractmethod
    def number(self):
        pass

    def iterate(self):
        self.current += 1
        self.values.append(entry(self.calculate(self.current), self.number()))

    def calculate(self,n):
        return int(self.calc(n))

    @abstractmethod
    def calc(self, n):
        pass

    def findPossible(self,figurate):
        if self == figurate: return
        for value in self.values:
            for foreign in figurate.values:
                self.test(value,foreign)

    def prune(self):
        for value in self.values:
            if len(value.possible) == 0:
                self.values.remove(value)

    def test(self, left, right):
        lDigs = Num2Dig(left.value)
        rDigs = Num2Dig(right.value)
        if lDigs[-2] == rDigs[0] and lDigs[-1] == rDigs[1]:
            left.possible.append(right)

    def find(self):
        for value in self.values:
            if len(value.possible) == 0: continue
            [check,output] = checkEntry(value,value,[8])
            if check:
                print(output)
        return [False,-1]


class Triangle(Figurate):
    def number(self):
        return 3

    def calc(self, n):
        return n * (n + 1) / 2


class Square(Figurate):
    def number(self):
        return 4

    def calc(self, n):
        return n ** 2


class Pentagon(Figurate):
    def number(self):
        return 5

    def calc(self, n):
        return n * (3 * n - 1) / 2


class Hexagon(Figurate):
    def number(self):
        return 6

    def calc(self, n):
        return n * (2 * n - 1)


class Septagon(Figurate):
    def number(self):
        return 7

    def calc(self, n):
        return n * (5 * n - 3) / 2


class Octogon(Figurate):
    def number(self):
        return 8

    def calc(self, n):
        return n * (3 * n - 2)

ideal = [3,4,5,6,7,8]

def checkEntry(initial,entry,used):
    for option in entry.possible:
        if option == initial and len(used) == 6 and option.value == initial.value:
            return [True, option.value]
        if not option.sides in used:
            cUsed = used[:]
            cUsed.append(option.sides)
            [check,chain] = checkEntry(initial,option,cUsed)
            if check:
                return [True, option.value + chain]
    return [False, -1]


if __name__ == "__main__":
    tri = Triangle()
    sq = Square()
    pen = Pentagon()
    hex = Hexagon()
    sept = Septagon()
    oct = Octogon()
    figs = [tri,sq,pen,hex,sept,oct]
    i = 1

    for fig in figs:
        for rem in figs:
            fig.findPossible(rem)
        fig.prune()
        i += 1

    output = oct.find()
    print(output)

# Answer: 28684
