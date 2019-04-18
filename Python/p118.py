from sympy import sieve
from MathPackage.NumberOperations import num2Dig
import sys

mySieve = {}

def nonRepeatingPrimes(n):
    primes = list(sieve.primerange(2, n))
    output = {}
    for prime in primes:
        digs = num2Dig(prime)
        s = set(digs)
        if 0 in s: continue
        if len(s) == len(digs):  # non repeating
            output[prime] = s
    return output

def count(primes,dict, start, currentSet):
    # print(currentSet)
    if len(currentSet) == 9:
        # print("}")
        return 1

    output = 0
    current = start
    for prime in primes[start:]:
        current += 1
        if len(currentSet) == 0:
            print(prime)
        if len(dict[prime].intersection(currentSet)) == 0:
            # print(str(prime) + ",",end='')
            newSet = currentSet.union(dict[prime])
            output += count(primes,dict, start, newSet)
    # print('')
    return output



if __name__ == '__main__':
    dict = nonRepeatingPrimes(1000000)
    primes = list(dict.keys())
    print('got primes')

    s = set()
    count(primes,dict, 0, s)
