from itertools import permutations
from math import log10,floor

def calculate():
    choice = range(0,10)
    output = 0
    for i in range(1,10000):
        power = 1
        while floor(log10(i ** power)) + 1 == power:
            if floor(log10(i ** power)) + 1 == power:
                output += 1
            power += 1
        if power == 1: break
    return output


if __name__ == "__main__":
    print calculate()
    print("Done")

# Answer: 49