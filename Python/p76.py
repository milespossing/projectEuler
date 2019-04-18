from math import floor

class Writer:
    def __init__(self):
        self.tab = 0

    def print(self, string):
        for i in range(0, self.tab): print("\t", end="", flush=True)
        print(string)

def f(m,n,s=""):
    if m < 0:
        return 0
    if n == 1:
        print(s + "11")
        return 1
    cs = s
    output = 0
    for i in range(1,n):
        cs = s + f"{str(i)} + "
        output += f(m-i,i,cs)
    print(f"Done with {str(m)}")
    return output

def c(m, n, writer, base=False):
    origin = n
    writer.print("c(" + str(m) + "," + str(n)+")")
    writer.tab += 1
    output = 1
    if n == m:
        output += 1
    if n > m:
        n = m
    if m == 0:
        writer.print("m=0")
        writer.tab -= 1
        return 0
    upper = m
    for i in range(2,upper):
        if m - i == 1:
            continue
        output += c(m - i, i, writer)
    writer.print("c("+str(m)+","+str(origin)+")="+str(output))
    writer.tab -= 1
    return output

if __name__ == '__main__':
    writer = Writer()
    print(f(5,5))