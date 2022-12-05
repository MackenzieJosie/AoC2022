stackInput, instructions = open("input.txt", "r").read().replace("["," ").replace("]"," ").split("\n\n")
stackInput = stackInput.split("\n")
instructions = instructions.split("\n")
instructions.pop()

stack = {}
for c in stackInput[len(stackInput)-1]:
    if c != " ":
        stack[int(c)] = [int(stackInput[len(stackInput)-1].index(c))]
stackInput.pop()

for line in reversed(stackInput):
    for num in stack:
        if line[stack[num][0]] != " ":
            stack[num].append(line[stack[num][0]])

# shifts = 0
for line in instructions:
    line = line.replace("move", "").replace("from", "-").replace("to", "-").replace(" ", "").split("-")
    line = [int(l) for l in line]
    for i in range(line[0],0,-1):
        stack[line[2]].append(stack[line[1]].pop(len(stack[line[1]])-i))

print(stack)