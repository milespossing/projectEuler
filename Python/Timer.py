import time

def timer(func):
    def fn():
        try:
            t1 = time.clock()
            func()
            t2 = time.clock()
            el = t2 - t1
            print(f"{round(el, 4)} seconds processing time ({round(el * 1000, 6)} ms)")
        except Exception as e:
            print(e)
    return fn