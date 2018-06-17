from __future__ import division
from NumberOperations import *
import ListOperations



def digitCanceled(a1,a2,n1,n2):
    c1 = 0
    if (IndexOf(a1, n1) != -1):
        c1 = a1[IndexOf(a1, n1) - 1]
    else: return False
    c2 = 0
    if (IndexOf(a2, n2) != -1):
        c2 = a2[IndexOf(a2, n2) - 1]
    else: return False
    if (c2 == c1 and c2 != 0):
        return True
    return False


output = 1


for den in range(10,100):
    for num in range(10,den):
        numF = Factor(num)
        denF = Factor(den)
        a1 = Num2Dig(num)
        a2 = Num2Dig(den)

        [numS, denS] = Dec2Frac(num / den)
        i = 1
        while (i * numS < num):
            if digitCanceled(a1, a2, numS*i, denS*i):
                output *= num / den
                break
            i += 1
        # common = ListOperations.both(numF, denF)
        # if len(common) == 0:
        #     continue
        # else:
        #     for f in common:
        #         n1 = num / f
        #         n2 = den / f
        #         output = digitCanceled()



#         [sNum,sDen] = Dec2Frac(num/den)

#         sNumDigs = Num2Dig(sNum)
#         sDenDigs = Num2Dig(sDen)

#
[outN,outD] = Dec2Frac(output)
print(outD)