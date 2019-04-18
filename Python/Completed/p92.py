from MathPackage.NumberOperations import num2Dig

reducers = set()

def chain(n):
    output = []
    digs = num2Dig(n)
    current = sum([dig ** 2 for dig in digs])
    while (not output.__contains__(current)):
        if current in reducers:
            output.append(89)
            return output
        output.append(current)
        digs = num2Dig(current)
        current = sum([dig ** 2 for dig in digs])
    return output


if __name__ == "__main__":
    output = 0
    for i in range(1, 10000000):
        c = chain(i)
        if c.__contains__(89):
            [reducers.add(v) for v in c]
            output += 1
        print(i)
    print(output)

# Answer: 8581146

# This one is solved in n log(n) time, I think. It's somewhat ambiguous because I short circuit things.
# Unfortunately n log(n) isn't quite fast enough for 10,000,000. I'm moving on for right now, but this one
# merits more work for sure
