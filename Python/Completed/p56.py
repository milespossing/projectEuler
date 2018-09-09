from MathPackage.NumberOperations import Num2Dig

output = 0

for i in range(1,100):
    for j in range(1,100):
        num = i ** j
        numA = Num2Dig(num)
        numS = sum(numA)
        if numS > output: output = numS

print(output)