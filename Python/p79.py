from MathPackage.NumberOperations import Num2Dig

def works(n):
    a = Num2Dig(n)
    for c in checks:
        if not test(a,Num2Dig(c)):
            return False
    return True

def test(test,check):
    c = 0
    for ch in check:
        while c < len(test):
            if ch == test[c]:
                break
            c += 1
        if c == len(test): return False
    return True


if __name__ == "__main__":
    f = open("files\\p79.txt")
    lines = f.readlines()
    f.close()
    checks = []
    for line in lines:
        checks.append(int(line.replace("\n","")))

    testNum = 111
    while not works(testNum):
        testNum += 1
        print(testNum)
    print(testNum)

