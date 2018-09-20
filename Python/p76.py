from math import floor

def alpha(a,n):
    i = 1
    output = 0
    while i * a < n:
        output += count(n - i * 1)
    for i in range(1,m + 1): #include m
        output += count(n - i * a)
    return output

n_vals = {}

def count(n):
    if n in n_vals: return n_vals[n]
    output = 1
    for i in range(2,n):
        output += alpha(i,n)
    n_vals[n] = output
    return output

if __name__ == '__main__':
    print(alpha(4,6))
    print(count(6))