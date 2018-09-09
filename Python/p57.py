from __future__ import division
from MathPackage.NumberOperations import Dec2Frac, DigCountLong as DigCount
from Timer import timer

def Solution():
    def GetExpansion(i):
        return 1 + recurse(i)

    def recurse(iter):
        if iter == 0: return 0
        return 1 / (2 + recurse(iter - 1))

    def GetExpansionFraction(count):
        outputNum = 1
        outputDen = 2
        for i in range(1, count):
            outputNum += 2 * outputDen
            temp = outputNum
            outputNum = outputDen
            outputDen = temp
        outputNum += outputDen
        return [outputNum, outputDen]

    output = 0
    for i in range(1, 1001):
        [num, den] = GetExpansionFraction(i)
        if DigCount(num) > DigCount(den):
            output += 1
        print(i)
    print(output)

# I think this algorithm works, but it's getting stuck up on the larger numbers
if __name__ == "__main__":
    timer(Solution)

# Answer: 153 in 0.237 seconds