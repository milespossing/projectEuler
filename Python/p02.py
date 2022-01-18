
class Fibonacci:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current == 0:
            self.current = 1
            self.last = 0
            return 1
        n = self.current + self.last
        if n > self.max:
            raise StopIteration
        self.last = self.current
        self.current = n
        return n

def solve():
    return sum([i for i in iter(Fibonacci(4000000)) if i % 2 == 0])

if __name__ == '__main__':
    print(solve())