# %% md
# Problem 95
# %% setup
import sympy
import numpy
from Timer import timer

N = 1000000
debug = False


def debug_print(val):
    if debug:
        print(val)


# %%

def get_factors():
    l = {}
    for i in range(2, N):
        a = sympy.primefactors(i)
        b = set(a)
        for factor in a:
            b.add(int(i / factor))
        b.add(1)
        # debug_print(f"{i}: {b}")
        l[i] = sum(b)
        # print(a)
    # debug_print(l)
    return l


def find_chains(l):
    visited = set()
    longestChain = []
    longest = 0
    for i in l:
        if i in visited:
            continue
        current = i
        currentSet = []
        good = False
        while current not in currentSet:
            visited.add(current)
            currentSet.append(current)
            current = l[current]
            if current == i:
                good = True
                break
            if current in visited:
                break
            if current >= N:
                break
        if not good:
            continue
        if len(currentSet) > longest:
            longest = len(currentSet)
            longestChain = currentSet
    return [longest, min(longestChain)]


@timer
def main():
    links = get_factors()
    [longest, smallest] = find_chains(links)
    print(f'longest={longest}\nsmallest={smallest}')


if __name__ == '__main__':
    main()

