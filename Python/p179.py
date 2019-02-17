from sympy import divisor_count

def divisors(n):
    f = divisor_count(n)
    return f

if __name__ == '__main__':
    last = 0
    output = 0
    for i in range(2,10000000):
        current = divisors(i)
        if current == last: output += 1
        last = current
    print(output)
