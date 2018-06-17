from numpy import log10

class node:
    def __init__(self):
        self.value = 0
        self.nextNode = None

    def add(self):
        index = 0
        output = 0
        current = self
        while index < 3:
            output += current.value
            current = current.nextNode
            index += 1
        return output

    def list(self):
        index = 0
        output = []
        current = self
        while index < 3:
            output.append(current.value)
            current = current.nextNode
            index += 1
        return output

class ring:
    def __init__(self):
        self.current = 0

        self.a = node()
        self.b = node()
        self.c = node()
        self.d = node()
        self.e = node()
        self.f = node()
        self.g = node()
        self.h = node()
        self.i = node()
        self.j = node()

        self.a.nextNode = self.b
        self.b.nextNode = self.c
        self.d.nextNode = self.c
        self.c.nextNode = self.e
        self.f.nextNode = self.e
        self.e.nextNode = self.g
        self.h.nextNode = self.g
        self.g.nextNode = self.i
        self.j.nextNode = self.i
        self.i.nextNode = self.b

        self.nodes = [self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h,self.i,self.j]
        self.outer = [self.a,self.d,self.f,self.h, self.j]

        self.values = [1,2,3,4,5,6,7,8,9,10]
        # self.values = [1,2,3,4,5,6]

    def makeRing(self,nodes,values):
        if len(values) > 1:
            for value in values:
                v = values[:]
                nodes[0].value = value
                v.remove(value)
                self.makeRing(nodes[1:],v)
        else:
            nodes[0].value = values[0]
            if (self.checkValues()):
                this = self.printValues()
                if this > self.current and log10(this) < 16: self.current = this


    def checkValues(self):
        first = self.a.add()
        if self.d.add() != first: return False
        if self.f.add() != first: return False
        if self.h.add() != first: return False
        if self.j.add() != first: return False
        return True

    def printValues(self):
        from operator import attrgetter
        lower = min(self.outer, key=attrgetter('value'))
        first = self.outer.index(lower)
        output = []
        for i in range(first,len(self.outer)):
            output.append(self.outer[i].list())
        for i in range(0,first):
            output.append(self.outer[i].list())
        return self.getValue(output)

    def getValue(self, arr):
        output = 0
        for a in arr:
            for i in a:
                if i < 10: output *= 10
                else: output *= 100
                output += i
        return output
        
    def printNodes(self):
        output = []
        output.append("a: " + str(self.a.value))
        output.append("b: " + str(self.b.value))
        output.append("c: " + str(self.c.value))
        output.append("d: " + str(self.d.value))
        output.append("e: " + str(self.e.value))
        output.append("f: " + str(self.f.value))
        output.append("g: " + str(self.g.value))
        output.append("h: " + str(self.h.value))
        output.append("i: " + str(self.i.value))
        output.append("j: " + str(self.j.value))
        return output
        

r = ring()
r.makeRing(r.nodes, r.values)
print(r.current)
print("done")
