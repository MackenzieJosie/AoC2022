# Opening file parsing the input and removing last empty line
input = open("input.txt").read().split("\n")
input.pop()

cycle = 0
X = 1
total = 0
value = 0

# function to multiply the cycle by the value in register X on cycles 20, 60, 100, 140, 180 and 220
def checkCycle(number):
	if number == 20 or ((number - 20) % 40) == 0:
		return number * X
	return 0

# main loop through cycles/commands
# if command is add, take an extra cycle
# calls checkCycle every time cycle is incremented to potentially add signal strength to the total
for line in input:
	cycle += 1
	total += checkCycle(cycle)
	if line[0] == "a":
		command, value = line.split(" ")
		value = int(value)
		cycle += 1
		total += checkCycle(cycle)
		X += value

# print solution		
print(total)