def makeNodes(vals):
    output = [Node(val) for val in vals]
    return output

class Node:

    def __init__(self, value):
        self.value = 0
        self.optimal = -1
        self.adjacent = []
        self.isBase = False
        self.value = value

    def setBase(self):
        self.optimal = self.value
        self.isBase = True

    def navigate(self):
        output = False
        if self.isBase: return
        for node in self.adjacent:
            if node.optimal == -1:
                continue
            if self.optimal == -1 or node.optimal + self.value < self.optimal:
                self.optimal = self.value + node.optimal
                self.next = node
                output = True
        return output


class Grid:
    def __init__(self, vals):
        self.nodes = []
        for row in vals:
            self.nodes.append(makeNodes(row))
        self.associate4()

    def iterate(self):
        hasChanges = False
        for row in self.nodes:
            for node in reversed(row):
                change = node.navigate()
                if change: hasChanges = True
        return hasChanges

    def solve(self):
        test = True
        while test:
            test = self.iterate()

    def associate2(self):
        for i in range(0, len(self.nodes)):
            for j in range(0, len(self.nodes[i])):
                if j < len(self.nodes[i]) - 1:
                    self.nodes[i][j].adjacent.append(self.nodes[i][j + 1])
                    if i > 0:
                        self.nodes[i][j].adjacent.append(self.nodes[i - 1][j])
                    if i < len(self.nodes) - 1:
                        self.nodes[i][j].adjacent.append(self.nodes[i + 1][j])
                else:
                    self.nodes[i][j].setBase()

    def associate4(self):
        for i in range(0, len(self.nodes)):
            for j in range(0, len(self.nodes[i])):
                if j < len(self.nodes[i]) - 1:
                    self.nodes[i][j].adjacent.append(self.nodes[i][j + 1])
                if j > 0:
                    self.nodes[i][j].adjacent.append(self.nodes[i][j-1])
                if i < len(self.nodes) - 1:
                    self.nodes[i][j].adjacent.append(self.nodes[i + 1][j])
                if i > 0:
                    self.nodes[i][j].adjacent.append(self.nodes[i - 1][j])
                if i == len(self.nodes) - 1 and j == len(self.nodes[i]) - 1:
                    self.nodes[i][j].setBase()

    def getSmallest(self):
        output = self.nodes[0][0].optimal
        for row in self.nodes:
            if row[0].optimal < output: output = row[0].optimal
        return output
