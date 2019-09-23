from collections import defaultdict

from Timer import timer


def get_attempts(path):
    f = open(path)
    output = []
    for line in f:
        data = line.replace("\n","")
        current = [int(c) for c in data]
        output.append(current)
    return output

def get_connection(attempt):
    l = len(attempt)
    for i in range(l - 1):
        for j in range(i + 1, l):
            yield attempt[i], attempt[j]

def make_number_graph(keylog):
    graph = defaultdict(set)
    for attempt in keylog:
        for a, b in get_connection(attempt):
            graph[a].add(b)
    return graph


def find_number_universe(keylog):
    numbers = set()
    for attempt in keylog:
        for num in attempt:
            numbers.add(num)
    return numbers

@timer
def p79():
    attempts = get_attempts("files/p79.txt")
    universe = find_number_universe(attempts)
    graph = make_number_graph(attempts)
    print(universe)
    print(graph)
    output = []
    while len(graph) > 0:


if __name__ == '__main__':
    p79()