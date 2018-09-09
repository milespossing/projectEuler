from sympy import primefactors

class tuple:
    def __init__(self, first):
        self.first = first
        self.second = primefactors(first)

class ArrayChecker:
    def __init__(self):
        self.currentTop = 647
        self.tuples = []
        self.append(644)
        self.append(645)
        self.append(646)
        self.append(647)

    def find(self):
        while self.notYet():
            self.iterate()
        return self.tuples[0].first

    def append(self, n):
        self.tuples.append(tuple(n))


    def iterate(self):
        self.tuples.remove(self.tuples[0])
        self.currentTop += 1
        self.tuples.append(tuple(self.currentTop))

    def notYet(self):
        for t in self.tuples:
            if len(t.second) != 4:
                self.fillFrom(t.first + 1)
                return True
        return False

    def fillFrom(self, n):
        del self.tuples[:]
        self.currentTop = n - 1
        for i in range(0, 4):
            self.currentTop += 1
            self.append(self.currentTop)




a = ArrayChecker()
out = a.find()
print(out)
