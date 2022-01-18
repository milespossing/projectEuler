import argparse

import p02, p03, p010, p38

def run(problem):
    if problem == 2: return p02.solve()
    elif problem == 3: return p03.solve()
    elif problem == 10: return p010.solve()
    elif problem == 38: return p38.solve()
    else: return -1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", help="problem", type=int)
    args = parser.parse_args()
    if (args.problem is not None):
        print(run(int(args.problem)))

