
class Code:
    def __init__(self):
        self.rules = set()
        self.code = []

    def addRule(self,rule):
        rules.append(rule)
        if len(self.code) == 0:
            self.code = rule.nums
        else:
            current = 0
            for num in rule.nums:
                if num in self.code[current:]:
                    current = self.code.index(num)
                else:
                    rules.insert(1,num)
                    current = 0

    def __repr__(self):
        return str(self.code)

class Rule:
    def __init__(self, nums=None):
        if nums is None:
            nums = []
        self.nums = nums

    def evaluate(self, code):
        current = 0
        for num in code:
            if num == self.nums[current]: current += 1
            if current == len(self.nums): return False
        return False

def check(code,rules):
    for rule in rules:
        if not rule.evaluate(code): return False
    return True


def build(rules):
    code = Code()
    for rule in rules:
        code.addRule(rule)
    return code



if __name__ == "__main__":
    f = open("files/p79.txt")
    lines = f.readlines()
    f.close()
    checks = []
    rules = []
    for line in lines:
        current = line.replace("\n","")
        arr = []
        for c in current:
            arr.append(int(c))
        rules.append(Rule(arr))
    code = []
    for r in rules:
        for val in r.nums:
            code.append(val)

    for i in range(len(code)):
        for j in range(i):
            if code[j] == code[i]:
                copy = code[:]
                copy.pop(j)
                if check(copy,rules):
                    code = copy
                    i = 0
    print("done")
