from numpy import log10
from MathPackage.NumberOperations import num2Dig, panArray

def first10(numA):
    return numA[:10]

def last10(numA):
    return numA[-10:]


if __name__ == "__main__":
    i = 2
    last = 1
    current = 1

    good = False
    test = False

    while not good:
        new = current + last
        last = current
        current = new
        i += 1
        if not test and log10(current) > 10:
            test = True
        if test:
            numA = num2Dig(current)
            good = panArray(first10(numA)) or panArray(last10(numA))
            print(current)

    print("Done")
    print(current)
    print(i)
