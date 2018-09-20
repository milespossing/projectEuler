from GeneralPackage.ListOperations import Copy2d
import numpy as np
from PathFinding import Grid

if __name__ == '__main__':
    f = open("files/p082.txt")

    rows = [row.split(",") for row in f]
    for row in rows:
        for j in range(0, len(row)):
            row[j] = int(row[j])
    f.close()

    g = Grid(rows)
    g.solve()
    print(g.nodes[0][0].optimal)

# 82: 260324
# 83: 425185