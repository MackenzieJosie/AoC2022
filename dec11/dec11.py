# Opening file parsing the input
monkeyInput = open("input.txt", "r").read().replace("M","m").replace(",", "").replace(":", "").split("\n\n")

monkeyInfo = {}
currentMonkey = ""

for monkey in monkeyInput:
    monkey = monkey.replace("  ","").split("\n")

    for item in monkey:
        if len(item) == 0: break
        match(item[0]):
            case "m":
                currentMonkey = item
                monkeyInfo[currentMonkey] = {}
                monkeyInfo[currentMonkey]["inspects"] = 0
            case "S":
                operations = item.split(" ")
                monkeyInfo[currentMonkey][operations[1]] = []
                for op in operations:
                    if op.isnumeric():
                        monkeyInfo[currentMonkey][operations[1]].append(int(op))
            case "O":
                operations = item.split("= ")
                monkeyInfo[currentMonkey]["Operation"] = operations[1]
            case "T":
                operations = item.replace("divisible by ", "").split(" ")
                monkeyInfo[currentMonkey][operations[0]] = int(operations[1])
            case "I":
                operations = item.replace("throw to ", "").split(" ")
                monkeyInfo[currentMonkey][operations[1]] = operations[2] + " " + operations[3]
# parsing done can print monkey info to ensure it is stored correctly
# print(monkeyInfo)

for i in range(20): # loop for number of rounds
    totalInspects = 0
    for monkey in monkeyInfo: # loop through each monkeys turn
        for old in monkeyInfo[monkey]["items"]: # loop for each item the monkey has
            monkeyInfo[monkey]["inspects"] += 1
            new = int(eval(monkeyInfo[monkey]["Operation"]) / 3) # decreasing worry level
            if new % monkeyInfo[monkey]["Test"] == 0:
                monkeyInfo[monkeyInfo[monkey]["true"]]["items"].append(new) # item is thrown to 'true'
            else:
                monkeyInfo[monkeyInfo[monkey]["false"]]["items"].append(new) # item is thrown to 'false'
        monkeyInfo[monkey]["items"] = [] # monkey has thrown all items, so empty the list
        totalInspects += monkeyInfo[monkey]["inspects"]

inspects = []
for monkey in monkeyInfo: # loop through monkeys to find highest two inspects
    inspects.append(monkeyInfo[monkey]["inspects"])

# sort to find highest number of inspects
inspects.sort(reverse=True)
print(inspects)

# print solution
print(inspects[0]*inspects[1])