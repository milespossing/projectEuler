from sympy import sieve, isprime, primerange, nextprime
from MathPackage.NumberOperations import combiner

def primeCheckRecursive(a, primes):
    if len(a) == 5:
        if isGood(a):
            return [True,a]
        return [False,a]
    else:
        for p in primes:
            a_copy = a[:]
            primes_copy = primes[:]
            primes_copy.remove(p)
            a_copy.append(p)
            if primeCheckRecursive(a_copy, primes_copy)[0]:
                return [True,a_copy]
        return [False, a_copy]

def primeCheckDynamic(maxNumber, currentArray):
    if len(currentArray) < 5:
        for p in primerange(currentArray[-1] + 1, maxNumber):
            if isGood(currentArray,p): # Move until a number can be added to the array
                copyArray = currentArray[:]
                copyArray.append(p)
                result = primeCheckDynamic(maxNumber, copyArray)
                if result[0]:
                    return result
        return [False,-1]
    else:
        return [True,sum(currentArray)]

def primeArray(n):
    output = []
    si = sieve
    for s in si.primerange(0,n):
        output.append(s)
    return output

def isGood(array,n):
    for a in array:
        if not (isprime(combiner(a,n)) and isprime(combiner(n,a))):
            return False
    return True

if __name__ == "__main__":
    min = 9999999
    for p in primerange(3,1000):
        print(p)
        result = primeCheckDynamic(10000,[p])
        if result[0] and result[1] < min:
            min = result[1]
            print("Good: " + str(p) + " with " + str(min))
    print(min)

# Correct Answer: 26033
