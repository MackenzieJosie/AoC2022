# Opening file parsing the input and removing last empty line
input = open("input.txt").read().split("\n")
input.pop()

cycle = 0
X = 1
value = 0

# if cycle is divisible by 40, print new line
def checkCycle(number):
	if ((number) % 40) == 0:
		print()

# main loop through cycles/commands
# prints either a lit or unlit char depending on the register X
# if command is add, take an extra cycle
# calls checkCycle after every print in case new line is needed
for line in input:
	cycle += 1
	if cycle % 40 == X or (cycle % 40) - 1 == X or (cycle % 40) - 2 == X:
		print("█", end="")
	else:
		print(".", end="")
	checkCycle(cycle)
	if line[0] == "a":
		command, value = line.split(" ")
		value = int(value)
		cycle += 1
		if cycle % 40 == X or (cycle % 40) - 1 == X or (cycle % 40) - 2 == X:
			print("█", end="")
		else:
			print(".", end="")
		checkCycle(cycle)
		X += value
		