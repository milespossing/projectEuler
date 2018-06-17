def Str2CharArr(s):
    return list(s)

def LetterNumber(s):
    num = ord(s)
    return num - 64

def LetterSum(st):
    output = 0
    for s in st:
        output += LetterNumber(s)
    return output
