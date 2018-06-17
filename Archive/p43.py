from PanDigitalOperator import PanDigitalOperator
from NumberOperations import Dig2Num
from sympy import isprime

op = PanDigitalOperator(10)

class p43:
    def __init__(self):
        self.output = 0

    def function(self, numA):

        if Dig2Num(numA[1:4]) % 2 != 0:
            return
        if Dig2Num(numA[2:5]) % 3 != 0:
            return
        if Dig2Num(numA[3:6]) % 5 != 0:
            return
        if Dig2Num(numA[4:7]) % 7 != 0:
            return
        if Dig2Num(numA[5:8]) % 11 != 0:
            return
        if Dig2Num(numA[6:9]) %13 != 0:
            return
        if Dig2Num(numA[7:10]) %17 != 0:
            return

        self.output += Dig2Num(numA)

p = p43()
op.iterate(p.function)
print(p.output)
print("Done")