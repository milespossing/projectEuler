from MathPackage.NumberOperations import num2Dig
import numpy as np
import math

loops = {}

def digFactorial(n):
    digs = num2Dig(n)
    return sum([math.factorial(dig) for dig in digs])

def chainer(n):
    chain = set()
    loop = []
    chain.add(n)
    loop.append(n)
    current = digFactorial(n)
    out = 0
    while not current in chain:
        if current in loops:
            out += loops[current]
            break
        chain.add(current)
        loop.append(current)
        current = digFactorial(current)
    out += len(chain)
    i = 0
    for link in loop:
        loops[link] = out - i
        i += 1
    return out

if __name__ == "__main__":
    output = 0
    for i in range(2,1000000):
        count = chainer(i)
        if count == 60: output += 1
        print(i)
    print(output)

# Answer: 402 in n log(n) time. Fast enough for 10^6, I think
