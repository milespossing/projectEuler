from collections import Counter

class character:
    def __init__(self,v,n):
        self.asci = v
        self.cipher = n

if __name__ == '__main__':
    f = open("../files/p59.txt")
    s = f.read()
    s.replace("\n","")
    arr = s.split(',')
    i = 0
    characters = []
    for a in arr:
        characters.append(character(int(a), i % 3))
        i += 1

    alpha = [a.asci for a in characters if a.cipher == 0]
    beta = [a.asci for a in characters if a.cipher == 1]
    gamma = [a.asci for a in characters if a.cipher == 2]
    a = Counter(alpha)
    b = Counter(beta)
    c = Counter(gamma)
    cipher = [a.most_common()[0][0] ^ ord(' '), b.most_common()[0][0] ^ ord(' '), c.most_common()[0][0] ^ ord(' ')]
    i = 0
    output = 0
    new = ""
    for a in characters:
        value = a.asci ^ cipher[i % 3]
        output += value
        new += chr(value)
        i += 1

    print(output)
    print(new)

# Answer: 107359