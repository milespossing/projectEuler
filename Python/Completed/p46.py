from sympy import sieve, isprime
from numpy import sqrt

sieve.extend(5)

current = 9
conjecture = True

while conjecture:
    while isprime(current):
        current += 2
    sieve.extend(current)
    isGood = False
    for i in sieve._list:
        if sqrt((current - i) / 2) % 1 == 0:
            isGood = True
            break
    if not isGood:
        print(current)
        conjecture = False
    current += 2

print("Done")

# Answer: 5777