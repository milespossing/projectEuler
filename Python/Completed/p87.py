from sympy import primerange

def buildPrimes(m):
    powers2 = []
    powers3 = []
    powers4 = []
    for p in primerange(1,m):
        if pow(p,2) > m:
            return [powers2,powers3,powers4]
        powers2.append(pow(p,2))
        temp = pow(p,3)
        if temp < m:
            powers3.append(temp)
        else:
            continue
        temp = pow(p,4)
        if temp < m:
            powers4.append(temp)
        else:
            a = 2 + 2

if __name__ == '__main__':
    m = 50 * pow(10,6)
    values = []
    output = 0
    [primes2, primes3, primes4] = buildPrimes(m)
    for p4 in primes4:
        for p3 in primes3:
            if p4 + p3 > m:
                break
            for p2 in primes2:
                if p2 + p3 + p4 < m:
                    output += 1
                    if (p2 + p3 + p4) in values:
                        print("Idiot")
                    values.append(p2 + p3 + p4)
                else:
                    break
            # values.sort()
    print(output)
    print(len(set(values)))