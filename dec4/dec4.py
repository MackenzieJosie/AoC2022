input = open("input.txt", "r").read().split("\n")

def part1(sum):
    for i in range(len(input)-1):
        ass = input[i].replace(",","-").split("-")
        if (int(ass[0]) >= int(ass[2]) and int(ass[1]) <= int(ass[3])) or (int(ass[2]) >= int(ass[0]) and int(ass[3]) <= int(ass[1])):
            sum += 1
    return sum

def part2(sum):
    for i in range(len(input)-1):
        ass = input[i].replace(",","-").split("-")
        if (int(ass[3]) >= int(ass[0]) >= int(ass[2])) or (int(ass[3]) >= int(ass[1]) >= int(ass[2])) or (int(ass[1]) >= int(ass[2]) >= int(ass[0])) or (int(ass[1]) >= int(ass[3]) >= int(ass[0])):
            sum += 1
    return sum

print(part1(0))
print(part2(0))

