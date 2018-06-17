def both(a,b):
    c = [i for i in a if i in (b)]
    return c

class ArrayPermuter:
    def __init__(self):
        self.output = []

    def permute(self, arr, current=[]):
        if len(arr) > 1:
            for a in arr:
                nArr = arr[:]
                nCurrent = current[:]
                nCurrent.append(a)
                nArr.remove(a)
                self.permute(nArr,nCurrent)
        else:
            current.append(arr[0])
            self.output.append(current)

def permute(arr):
    a = ArrayPermuter()
    a.permute(arr)
    return a.output