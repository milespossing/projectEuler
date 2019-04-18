if __name__ == '__main__':
    f = open("files/p99.txt")
    lines = f.readlines()
    output = []
    for line in lines:
        current = line.replace("\n","").split(",")
        output.append([int(current[0]),int(current[1])])
    m = 0
    i = 0
    index = 0
    for line in output:
        current = pow(line[0],line[1],pow(10,1000))
        if current > m:
            m = current
            index = i
        i += 1
    print(m)
    print(index)
