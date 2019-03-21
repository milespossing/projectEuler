class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

def triangleArea(p1,p2,p3):
    area = abs((p1.x*(p2.y-p3.y)+p2.x*(p3.y-p1.y)+p3.x*(p1.y-p2.y))/2)
    return area

def hasOrigin(p1,p2,p3):
    origin = Point()
    area1 = triangleArea(origin,p1,p2)
    area2 = triangleArea(origin,p2,p3)
    area3 = triangleArea(origin,p1,p3)
    totalArea = triangleArea(p1,p2,p3)

    if area1 + area2 + area3 > totalArea: return False
    return True

def parseLine(line):
    data = line.split(",")
    p1 = Point(int(data[0]),int(data[1]))
    p2 = Point(int(data[2]),int(data[3]))
    p3 = Point(int(data[4]),int(data[5]))
    return [p1,p2,p3]


if __name__ == '__main__':
    f = open("./files/p102.txt")
    data = []
    output = 0
    for line in f:
        data.append(parseLine(line))
    for set in data:
        has = hasOrigin(set[0],set[1],set[2])
        if has: output += 1
    print("Answer: " + str(output))

# correct answer: 228