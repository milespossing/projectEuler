import time

def timer(func):
    t1 = time.clock()
    func()
    t2 = time.clock()
    print(t2 - t1, " seconds processing time")