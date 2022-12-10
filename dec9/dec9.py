input = open("input.txt", "r").read().split("\n")
#initializing variables
tailVisited = {}
headX, headY = 100, 150
tailX, tailY = 100, 150
tempX, tempY = 0, 0

# function to get dict key based on tail coordinates
def positionToString(tailX, tailY):
    return str(tailX) + "," + str(tailY)

tailVisited[positionToString(tailX, tailY)] = 1

for line in input:
    if len(line) == 0:
        break

    direction, distance = line.split(" ")
    distance = int(distance)

    for i in range(distance):
        tempX, tempY = headX, headY
        match(direction):
            case "U":
                headY += 1
            case "D":
                headY -= 1
            case "R":
                headX -= 1
            case "L":
                headX += 1

        if abs(headX - tailX) > 1 or abs(headY - tailY) > 1:
            tailX, tailY = tempX, tempY
            if positionToString(tailX, tailY) not in tailVisited:
                tailVisited[positionToString(tailX, tailY)] = 1

print(len(tailVisited))

# this draws the path taken by the tail
# for i in range(0,400):
#     for j in range(0,400):
#         if positionToString(i, j) in tailVisited:
#             print("#", end="")
#         else:
#             print(".",end="")
#     print()

