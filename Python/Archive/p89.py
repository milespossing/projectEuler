class NumeralWriter:
    def reduce(self, n):
        output = ""
        if n > 1000:
            while n > 1000:
                output += "M"
                n -= 1000
            return output + self.reduce(n)
        elif n >= 100:
            if n >= 900:
                return "CM" + self.reduce(n - 900)
            if n >= 500:
                return "D" + self.reduce(n - 500)
            if n >= 400:
                return "CD" + self.reduce(n - 400)
            while n >= 100:
                output += "C"
                n -= 100
            return output + self.reduce(n)
        elif n >= 10:
            if n >= 90:
                return "XC" + self.reduce(n - 90)
            if n >= 50:
                return "L" + self.reduce(n - 50)
            if n >= 40:
                return "XL" + self.reduce(n - 40)
            while n >= 10:
                output += "X"
                n -= 10
            return output + self.reduce(n)
        else:  # n is less than 10
            if n == 9:
                return "IX"
            if n >= 5:
                output += "V"
                n -= 5
            elif n == 4:
                return output + "IV"
            while n > 0:
                output += "I"
                n -= 1
            return output

    def parse(self, numeral):
        output = 0
        if len(numeral) == 0:
            return 0
        elif numeral[0] == "M":
            [o, current] = self.__parse__(numeral, "M", 1000)
            output += o
            return output + self.parse(numeral[current:])
        elif numeral[0] == "C":
            if len(numeral) > 1:
                if numeral[1] == "M":
                    return 900 + self.parse(numeral[2:])
                elif numeral[1] == "D":
                    return 400 + self.parse(numeral[2:])
                else:
                    [o, current] = self.__parse__(numeral,"C",100)
                    return o + self.parse(numeral[current:])
            else: return 100
        elif numeral[0] == "X":
            if len(numeral) > 1:
                if numeral[1] == "C":
                    return 90 + self.parse(numeral[2:])
                elif numeral[1] == "L":
                    return 40 + self.parse(numeral[2:])
                else:
                    [o, current] = self.__parse__(numeral,"X",10)
                    return o + self.parse(numeral[current:])
            else: return 10
        elif numeral[0] == "V":
            return 5 + self.parse(numeral[1:])
        elif numeral[0] == "L":
            return 50 + self.parse(numeral[1:])
        elif numeral[0] == "D":
            return 500 + self.parse(numeral[1:])
        elif numeral[0] == "I":
            if len(numeral) > 1:
                if numeral[1] == "X":
                    return 9 + self.parse(numeral[2:])
                elif numeral[1] == "V":
                    return 4 + self.parse(numeral[2:])
                else:
                    [o, current] = self.__parse__(numeral,"I",1)
                    return o + self.parse(numeral[current:])
            else: return 1
        else: return 0

    def __parse__(self, numeral, target, value):
        current = 0
        output = 0
        while current < len(numeral) and numeral[current] == target:
            output += value
            current += 1
        return [output, current]


if __name__ == "__main__":
    n = NumeralWriter()
    f = file("files\\p89.txt")
    lines = f.readlines()
    output = 0
    for line in lines:
        current = line.replace("\n","")
        length = len(current)
        number = n.parse(current)
        real = n.reduce(number)
        real_len = len(real)
        difference = real_len - length
        output += difference
    print(output)