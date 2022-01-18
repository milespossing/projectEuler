from sympy import sieve

def solve():
    return sum(sieve.primerange(2000000))

if __name__ == '__main__':
    print(solve())