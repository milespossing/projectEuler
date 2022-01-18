from sympy import primefactors

def solve():
    return max(primefactors(600851475143))

if __name__ == '__main__':
    print(solve())