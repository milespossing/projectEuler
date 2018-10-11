from math import floor

class Writer:
    def __init__(self):
        self.tab = 0

    def print(self, string):
        for i in range(0, self.tab): print("\t", end="", flush=True)
        print(string)

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
    c(8, 8, writer)