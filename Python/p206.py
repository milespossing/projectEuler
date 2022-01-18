import math
from Timer import timer
from MathPackage.NumberOperations import num2Dig

def checkNumber(num):
    digs = num2Dig(num)
    for i in range(0,9):
        if digs[i * 2] != i + 1: return False
    if digs[-1] != 0: return False
    return True


def p206():
    number = math.floor(math.sqrt(pow(10.0102, 19)))
    check = checkNumber(number**2)
    while not check:
        print(number**2)
        number += 1
        check  = checkNumber(number**2)
    print(f"Solution: {number}")

if __name__ == '__main__':
    p206()
