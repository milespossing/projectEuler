import numpy as np

nodes = [0]
count = 0

class link:
    def __init__(self, value, row, col):
        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return f"[{self.row}][{self.col}];{self.value};"

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.value < other.value

def getPossibleLinks(newData,oldData):
    output = []
    for row in nodes:
        for i in range(0,count):
            val = oldData[row][i]
            if val > 0 and i not in nodes:
                l = link(val,row,i)
                output.append(l)
    output.sort()
    return output

def getMatrix(lines):
    output = []
    for line in lines:
        cleanLine = line.replace("\n","")
        cells = cleanLine.split(",")
        current = []
        for cell in cells:
            if cell == "-": current.append(0)
            else: current.append(int(cell))
        output.append(current)
    return output

def makeEmpty(length):
    output = []
    for i in range(0,length):
        current = []
        for j in range(0,length):
            current.append(0)
        output.append(current)
    return output

def isComplete():
    return len(nodes) == count

def useLink(link):
    empty[link.row][link.col] = link.value
    empty[link.col][link.row] = link.value
    data[link.row][link.col] = 0
    data[link.col][link.row] = 0
    if link.col not in nodes: nodes.append(link.col)

def matSumTop(mat):
    output = 0
    for row in mat:
        output += sum(row)
    return output

def matSumFull(mat):
    return int(matSumTop(mat) / 2)

if __name__ == '__main__':
    f = open("./files/p107.txt")
    data = getMatrix(f)
    top = (matSumFull(data))
    count = len(data)
    empty = makeEmpty(len(data))
    print(np.matrix(data))
    while not isComplete():
        possibles = getPossibleLinks(empty,data)
        useLink(possibles[0])
    bottom = (matSumFull(empty))
    print(top)
    print(bottom)
    print(top - bottom)
    # newMat = np.matrix(fullMat.)