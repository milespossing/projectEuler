from __future__ import division

from MathPackage.NumberOperations import num2Dig
from Timer import timer

def is_bouncy(n):
    has_inc, has_dec = False,False
    rightNum = n % 10
    n = n // 10
    while n > 0:
        leftNum = n % 10
        if leftNum > rightNum: has_inc = True
        elif leftNum < rightNum: has_dec = True
        n = n // 10
        rightNum = leftNum
    if has_dec and has_inc: return True
    return False


def bouncy(n):
    digs = num2Dig(n)
    current = 0
    if len(set(digs)) == 1: return True
    sDigs = sorted(digs)
    if sDigs == digs: return False
    sDigs.reverse()
    if sDigs == digs: return False
    return True

@timer
def main():
    count = 0
    current = 99
    while count < .99 * current:
        current += 1
        if is_bouncy(current): count += 1
        print(str(current) + ": " + str(count / current))


if __name__ == '__main__':
    main()
