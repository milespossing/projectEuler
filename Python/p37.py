from sympy import prime, isprime, sieve, primerange
from numpy import ceil, log10

def left(num):
    isGood = True
    while num > 0 and isGood:
        isGood = num in sieve
        num /= 10
    return isGood

def right(num):
    isGood = True
    i = ceil(log10(num))
    while i > 0 and isGood:
        num = int(num % pow(10,i))
        isGood = num in sieve
        i -= 1
    return isGood

test = right(3797)

# print("Finding primes...")
#
# print("Found primes...")
primes = []
i = 5

for i in primerange(20,9999999):
    if len(primes) >= 11: break
    if left(i) and right(i):
        primes.append(i)
        print("Found " + str(i))
        print(str(len(primes)) + " / 11 found")

# while len(primes) < 11:
#     current = prime(i)
#     if left(current) and right(current):
#         primes.append(current)
#         print("Found " + str(current))
#         print(str(len(primes)) + " / 11 found")
#     i += 1

print(primes)

print(sum(primes))
