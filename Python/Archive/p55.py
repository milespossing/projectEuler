from MathPackage.NumberOperations import isPalindrome, reverse

def testLychrel(num):
    num = num + reverse(num)
    i = 0
    while not isPalindrome(num):
        num = num + reverse(num)
        i += 1
        if i == 50: return True
    return False

count = 0
for i in range(11,10000):
    print(i)
    if testLychrel(i):
        count += 1

print(count)