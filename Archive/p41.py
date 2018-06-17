from sympy import isprime
from NumberOperations import Num2Dig

master = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def panDigital(num):
    arr = Num2Dig(num)
    for i in range(1,len(arr) + 1):
        count = 0
        for a in arr:
            if i == a:
                count += 1
        if count != 1:
            return False
    return True

def test(num, arr):
    arr = list(arr)
    if len(arr) > 1:
        for a in arr:
            currentA = arr[:]
            current = num * 10 + a
            currentA.remove(a)
            if (test(current,currentA)): return True
    else:
        current = num * 10 + arr[0]
        print(current)
        if isprime(current) and panDigital(current):
            print(current)
            return True
        return False


while not test(0,master):
    master.remove(master[0])