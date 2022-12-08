input = open("input.txt", "r").read().split("\n")
input.pop() # to remove empty last line

treeMap = [[0 for j in range(len(input))] for i in range(len(input))]

# Building the map
i = 0
for line in input:
    j = 0
    for char in line:
        treeMap[i][j] = int(char)
        j += 1
    i += 1

# checking if the tree is visible for part 1
def isVisible(path, tree, direction):
    for pathTree in path:
        if pathTree >= tree:
            return 0

    # print(path, tree, direction) # used direction for debugging
    return 1

# checking how many trees are visible for part 2
def numVisible(path, tree, direction):
    highest, total = 0, 0

    if direction == "left" or direction == "up":
        path = reversed(path)

    for pathTree in path:
        if pathTree >= tree:
            return total + 1
        else:
            total += 1

    return total

# traversing map and counting visible trees
totalVisible = 0
highScore = 0
for i in range(len(treeMap)):
    for j in range(len(treeMap[i])):
        currentScore = 0
        if i == 0 or i == len(treeMap)-1 or j == 0 or j == len(treeMap[i])-1:
            totalVisible += 1
        else:
            above, below = [], []
            for k in range(0,i):
                above.append(treeMap[k][j])
            for k in range(i+1,len(treeMap)):
                below.append(treeMap[k][j])
            totalVisible += isVisible(treeMap[i][:j], treeMap[i][j], "left") or isVisible(treeMap[i][j+1:], treeMap[i][j], "right") or isVisible(above, treeMap[i][j], "up") or isVisible(below, treeMap[i][j], "down")
            currentScore = numVisible(treeMap[i][:j], treeMap[i][j], "left") * numVisible(treeMap[i][j+1:], treeMap[i][j], "right") * numVisible(above, treeMap[i][j], "up") * numVisible(below, treeMap[i][j], "down")
            if currentScore > highScore:
                highScore = currentScore

print("Total visible trees:", totalVisible)
print("Highscore:", highScore)

