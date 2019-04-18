from Timer import timer

@timer
def Solution():
    f = open("../files/p081.txt")
    rows = [row.split(",") for row in f]
    for row in rows:
        for i in range(0, len(row)):
            row[i] = int(row[i])
    i = len(rows) - 1
    j = len(rows[0]) - 1
    maxi = i
    maxj = j
    while i >= 0:
        while j >= 0:
            down = -1
            right = -1
            if i < maxi:
                down = rows[i + 1][j]
            if j < maxj:
                right = rows[i][j + 1]
            if down == -1 and right == -1:
                j -= 1
                continue
            elif down == -1:
                rows[i][j] += right
            elif right == -1:
                rows[i][j] += down
            else:
                if right < down:
                    rows[i][j] += right
                else:
                    rows[i][j] += down
            j -= 1
        i -= 1
        j = len(rows[0]) - 1
    print(rows[0][0])

if __name__ == "__main__":
    Solution()

# Answer: 427337 (computed in linear time, 17ms)
