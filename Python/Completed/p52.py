from MathPackage.NumberOperations import isPermutation
from Timer import timer



def works(num):
    for i in range(2,7):
        if not isPermutation(num,i * num):
            return False
    return True

@timer
def main():
    good = False
    current = 1
    while not good:
        current += 1
        if works(current):
            good = True
    print(current)

if __name__ == '__main__':
    main()

# Answer: 142857