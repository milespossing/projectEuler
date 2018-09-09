from sympy import sieve
from MathPackage.NumberOperations import isPermutation

def commonDifferent(arr):
    for i in range(0,len(arr)):
        current = arr[i]
        for j in range(i + 1, len(arr)):
            current2 = arr[j]
            for k in arr[j + 1:]:
                if k - current2 == current2 - current:
                    return [current,current2,k]
    return -1

primes = []

for p in sieve.primerange(1000,9999):
    primes.append(p)

permutations = []
i = 0
while i < len(primes):
    current = primes[i]
    currentList = [current]
    for p2 in primes[i + 1:]:
        if isPermutation(current,p2):
            currentList.append(p2)
            primes.remove(p2)
    if len(currentList) >= 3: permutations.append(currentList)
    i += 1

for a in permutations:
    if commonDifferent(a) != -1:
        print(commonDifferent(a))

print("Done")

# Answer: [2969, 6299, 9629]
