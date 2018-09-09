from GeneralPackage.ListOperations import Copy2d
import numpy as np

f = open("files/p082.txt")

rows = [row.split(",") for row in f]
for row in rows:
    for j in range(0, len(row)):
        row[j] = int(row[j])
f.close()
rows = np.array(rows)
minSum = rows.copy()
m = rows.shape[0]
n = rows.shape[1]
j = m - 2

while j >= 0:
    i = 0
    while i < n:
        minSum[i, j] += minSum[i, j + 1]
        i += 1
    i = 0
    while i < n:
        currentMin = minSum[i, j]
        index = i
        # This algorithm needs to keep on moving upwards before moving forwards
        while i != 0 and :
            u = rows[i, j] + minSum[i - 1, j]
            if minSum[i, j] > u:
                minSum[i, j] = u
        if i < n - 1:
            d = rows[i, j] + minSum[i + 1, j]
            if minSum[i, j] > d:
                minSum[i, j] = d
        i += 1
    j -= 1

output = minSum[0, 0]
for row in minSum:
    if row[0] < output: output = row[0]
print(output)
