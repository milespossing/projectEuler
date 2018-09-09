# from __future__ import division

output = []

class pentagonal:
    def pentagon(self, n):
        return n * (3 * n - 1) / 2

    def __init__(self):
        self.arr = []
        self.length = 0
        self.i = 1
        self.extendN(2)

    def extend(self):
        self.length += 1
        self.arr.append(self.pentagon(self.length))

    def iterate(self):
        current = self.arr[self.i]
        self.i += 1
        hasNone = True
        for i in self.arr[:self.i - 1]:
            low = current - i
            high = current + i
            while high > self.getMax():
                self.extendN(2)
            if self.inArray(low) and self.inArray(high):
                print(low)
                return low
        if hasNone: return -1


    def extendN(self, i):
        for i in range(0, i):
            self.extend()

    def getMax(self):
        return self.arr[-1]

    def inArray(self, n):
        return n in self.arr


p = pentagonal()
while p.iterate() == -1:
    print(p.getMax())

print("Done")
# output = []
#
# p = []
#
# for i in range(1,1500):
#     print(str(i) + ": " + str(pentagon(i)))
#     p.append(pentagon(i))
#     for j in reversed(p):
#         if i - j in p:
#             output.append([i,j,i-j,i+j])
#
# mini = 999999999
#
# for i in output:
#     if i[3] in p and i[2] < mini:
#         mini = i[2]
#
# print(mini)
