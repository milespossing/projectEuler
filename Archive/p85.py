t = 2000000

def dif(n):
    return abs(t - n)

def count(m,n):
    return (m*(m + 1) * n * (n + 1)) / 4

def pack(x,y):
    return [x,y,count(x,y)]

x = 1
y = 1
best = pack(x,y)
while count(x,1) < t:
    y = 1
    current = pack(x,y)
    while count(x,y) < t:
        y += 1
        n = pack(x,y)
        if dif(n[2]) < dif(current[2]):
            current = n
    if dif(current[2]) < dif(best[2]):
        best = current
    print("Best" + str(best))
    print("Current" + str(current))
    x += 1

print(best)
print(best[0] * best[1])

# Answer: 2772
