from numpy import log
from ListOperations import permute
from NumberOperations import Num2Dig, Dig2Num
import collections
import datetime

start = datetime.datetime.now()

notYet = True
current = 400
currentList = []
currentMax = 100

cube = current ** 3

def isCube(num):
    return (log(num)/log(3)) % 1 == 0

# print(isCube(26))

while notYet:
    #gather all cubes in this base
    print("Base: " + str(currentMax))
    while cube < currentMax:
        currentList.append(Num2Dig(cube))
        current += 1
        cube = current ** 3
    for i in range(0, len(currentList) - 3):
        count = 1
        c = currentList[i]
        for j in currentList[i + 1:]:
            if collections.Counter(c) == collections.Counter(j):
                count += 1
                if count > 5: break
        if count == 5:
            notYet = False
            print(Dig2Num(c))
            break
    currentMax *= 10
    currentList = []

print(datetime.datetime.now() - start)