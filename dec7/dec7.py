input = open("input.txt", "r").read().split("\n")
input.pop() # to remove empty last line

directories = {}
currentPath = []
sum = 0

def pathToString(currentPath):
    currentPathString = "".join(currentPath)
    return currentPathString 

for line in input:
    if line[0] == '$':  # command
        if line[2:4] == "cd":
            if line[5:7] == "..": # going back in directory, adding total of current directory to the destination directory
                temp = directories[pathToString(currentPath)]
                currentPath.pop()
                directories[pathToString(currentPath)] += temp
            elif line[5] == "/": # initializing the directory structure
                currentPath = ["/"]
                directories["/"] = 0
            else: # changing the current path to reflect the cd command
                if len(currentPath) > 1:
                    currentPath.append("/"+line[5:])
                else:
                    currentPath.append(line[5:])
    else:  # output of ls
        dirOrSize, name = line.split(" ")
        if dirOrSize[0].isnumeric(): # its a file, add size to the current directory
            dirOrSize = int(dirOrSize)
            directories[pathToString(currentPath)] += dirOrSize
        else: # its a directory, initialize member of dict for directory
            if len(currentPath) > 1:
                directories[pathToString(currentPath)+"/"+name] = 0
                # could intialize and store directories as dictionaries to be able to store the individual files in data as well
                # however this is not required for the problem so we just need to keep track of the size
            else:
                directories[pathToString(currentPath)+name] = 0

while currentPath != ["/"]: # to similuate using "cd .." back down to root at end to add sizes back to the directories they are contained in
    temp = directories[pathToString(currentPath)]
    currentPath.pop()
    directories[pathToString(currentPath)] += temp

# per the part 1 problem
for item in directories:
    if directories[item] < 100000:
        sum += directories[item]

print(sum) # part 1 solution

# set up values needed for part 2
goal = 70000000 - directories["/"]
goal = 30000000 - goal
best = 30000000

# per the part 2 problem
for item in directories:
    if goal < directories[item] < best:
        best = directories[item]

print(best) # part 2 solution
