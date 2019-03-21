from sympy import primerange, isprime, primefactors
from numpy import gcd

if __name__ == "__main__":
    n = 1000000
    output = 0
    for i in range (2,n + 1):
        for j in range(1,i):
            if gcd(i,j) == 1:
                output += 1
        print(i)
    print("output: " + str(output))

    # output = n - 1 # all numbers have 1/n apart from 1
    # primes = 1 # primes less than 3
    # for i in range(3,n + 1):
    #     if isprime(i): # if i is prime we add i - 2 to the output as we've already counted 1/i and don't count i/i
    #         primes += 1 # there's one more prime < i
    #         output += i - 2 # see above
    #     else: # number is not prime
    #         output += primes - len(primefactors(i))
    #     print(i)
    print("Count: " + str(output))