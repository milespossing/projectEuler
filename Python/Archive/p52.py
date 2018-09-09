from MathPackage.NumberOperations import isPermutation

good = False
current = 1

def works(num):
    for i in range(2,7):
        if not isPermutation(num,i * num):
            return False
    return True

while not good:
    current += 1
    if works(current):
        good = True

print(current)

# Answer: 142857