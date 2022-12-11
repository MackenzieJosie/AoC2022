# input parsing
# monkeyInput = open("example.txt", "r").read().replace("M","m").replace(",", "").replace(":", "").split("\n\n")
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
# parsing done
# print(monkeyInfo)

for i in range(20): # loop for number of rounds
    totalInspects = 0
    for monkey in monkeyInfo: # loop through each monkeys turn
        # print(monkeyInfo[monkey])
        for old in monkeyInfo[monkey]["items"]: # loop for each item the monkey has
            monkeyInfo[monkey]["inspects"] += 1
            new = int(eval(monkeyInfo[monkey]["Operation"]) / 3)
            # print(new)
            if new % monkeyInfo[monkey]["Test"] == 0:
                monkeyInfo[monkeyInfo[monkey]["true"]]["items"].append(new)
            else:
                monkeyInfo[monkeyInfo[monkey]["false"]]["items"].append(new)
        monkeyInfo[monkey]["items"] = []
        totalInspects += monkeyInfo[monkey]["inspects"]

inspects = []
for monkey in monkeyInfo: # loop through monkeys to find highest two inspects
    inspects.append(monkeyInfo[monkey]["inspects"])

inspects.sort(reverse=True)
print(inspects)

print(inspects[0]*inspects[1])