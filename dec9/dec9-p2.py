# Opening file parsing the input
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

# main loop through input
for line in input:
    if len(line) == 0:
        break

    direction, distance = line.split(" ")
    distance = int(distance)

    # moving head in the direction and distance specified
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
 
        # moving all 9 tails to keep them touching
        for i in range(0,9):
            xDif = knotsX[i] - knotsX[i+1]
            yDif = knotsY[i] - knotsY[i+1]
            if abs(xDif) > 1: # difference in X value is too far, need to move the next tail
                if xDif > 0: knotsX[i+1] += 1
                if xDif < 0: knotsX[i+1] -= 1
                # now need to see if the Y also needs to change
                if abs(yDif) > 0:
                    if yDif > 0: knotsY[i+1] += 1
                    if yDif < 0: knotsY[i+1] -= 1
            # same as above but swap x's and y's
            elif abs(yDif) > 1:
                if yDif > 0: knotsY[i+1] += 1
                if yDif < 0: knotsY[i+1] -= 1
                if abs(xDif) > 0:
                    if xDif > 0: knotsX[i+1] += 1
                    if xDif < 0: knotsX[i+1] -= 1

        # keeping track of which locations the tail has visited
        if positionToString(knotsX[9], knotsY[9]) not in tailVisited:
            tailVisited[positionToString(knotsX[9], knotsY[9])] = 1
    lineNumber += 1

print(len(tailVisited)) # solution

# this draws the path taken by the tail for debugging purposes and also its cool
# for i in range(-250,70):
#     for j in range(-200,100):
#         if positionToString(i, j) in tailVisited:
#             print("#", end="")
#         else:
#             print(".",end="")
#     print()