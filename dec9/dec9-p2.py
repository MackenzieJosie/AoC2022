input = open("input.txt", "r").read().split("\n")
#initializing variables
tailVisited = {}
knotsX, knotsY = [], []
for i in range(10):
    knotsX.append(15)
    knotsY.append(11)
lineNumber = 1

# function to get dict key based on tail coordinates
def positionToString(x, y):
    return str(x) + "," + str(y)

tailVisited[positionToString(knotsX[9], knotsY[9])] = 1

for line in input:
    if len(line) == 0:
        break

    direction, distance = line.split(" ")
    distance = int(distance)

    for i in range(distance):
        match(direction):
            case "U":
                knotsY[0] -= 1
            case "D":
                knotsY[0] += 1
            case "R":
                knotsX[0] += 1
            case "L":
                knotsX[0] -= 1
 
        for i in range(0,9):
            xDif = knotsX[i] - knotsX[i+1]
            yDif = knotsY[i] - knotsY[i+1]
            if abs(xDif) > 1:
                if xDif > 0: knotsX[i+1] += 1
                if xDif < 0: knotsX[i+1] -= 1

                if abs(yDif) > 0:
                    if yDif > 0: knotsY[i+1] += 1
                    if yDif < 0: knotsY[i+1] -= 1
            elif abs(yDif) > 1:
                if yDif > 0: knotsY[i+1] += 1
                if yDif < 0: knotsY[i+1] -= 1
                if abs(xDif) > 0:
                    if xDif > 0: knotsX[i+1] += 1
                    if xDif < 0: knotsX[i+1] -= 1

        if positionToString(knotsX[9], knotsY[9]) not in tailVisited:
            tailVisited[positionToString(knotsX[9], knotsY[9])] = 1
    lineNumber += 1

print(len(tailVisited))

# this draws the path taken by the tail
# for i in range(0,30):
#     for j in range(0,30):
#         if positionToString(i, j) in tailVisited:
#             print("#", end="")
#         else:
#             print(".",end="")
#     print()

