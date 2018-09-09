from sympy import primerange, isprime
from MathPackage.NumberOperations import Num2Dig, Dig2Num
from itertools import combinations

def replace(num):
    print(num)
    places = 1
    numA = Num2Dig(num)
    possiblePlaces = range(0, len(numA) - 1)
    while places < len(numA):
        check = recurse(numA,places,possiblePlaces)
        if check:
            return True
        places += 1
    return False

def recurse(a,n,possiblePlaces):
    for places in combinations(possiblePlaces, n):
        count = 0
        primes = []
        if 0 in places: minVal = 1
        else: minVal = 0
        aCopy = a[:]
        for v in range(minVal, 10):
            for place in places:
                aCopy[place] = v
            if isprime(Dig2Num(aCopy)):
                count += 1
                primes.append(Dig2Num(aCopy))
        if count >= 8:
            return True
    return False

good = False
i = 0
for i in primerange(2,10000000):
    good = replace(i)
    if good: break

# Answer: 121313 <- found with some extra deduction by breakpoint, the first prime found with this quality is not the correct answer.
#                   I should have returned the first value of the primes list made on line 20
