import numpy
import sympy
import Timer

def closest(num,d):
    output = numpy.floor(num*d)
    return output


def logic():
    target = 3 / 7
    maxD = 1000000
    currentleft = 0
    N = 0
    D = 1
    d = 2
    n = 1
    while d <= maxD:
        d += 1
        currentN = closest(currentleft, d)
        reduced = 0
        while (n + 1) / d < target:
            n += 1
            if numpy.gcd(n, d): reduced = n
        if reduced / d > currentleft:
            currentleft = reduced / d
            N = reduced
            D = d
    print(str(N) + " / " + str(D))


if __name__ == '__main__':
    Timer.timer(logic)
    # Answer?: 428570