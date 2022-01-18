from numpy import log10,ceil
from MathPackage.NumberOperations import hasDuplicates, panDigital

def makeNumber(num):
    output = num
    n = 1
    while log10(output) < 9:
        new = num * (n + 1)
        if ceil(log10(new)) + ceil(log10(output)) > 9:
            break
        n += 1
        output *= int(pow(10,ceil(log10(new))))
        output += new
        if hasDuplicates(output):
            return [n,-1]
    return [n,output]

def solve():
    i = 3
    high = 0
    current = makeNumber(i)
    while (current[1] == -1):
        i += 2
        current = makeNumber(i)

    while(current[0] > 1):
        if panDigital(current[1]):
            if current[1] > high: high = current[1]
        i += 2
        current = makeNumber(i)
        while (current[1] == -1):
            i += 2
            current = makeNumber(i)
    return high

if __name__ == '__main__':
    print(solve())