input = open("input.txt").read().split("\n")
input.pop()

cycle = 0
X = 1
value = 0

def checkCycle(number):
	if ((number) % 40) == 0:
		print()

for line in input:
	cycle += 1
	if value:
		X+= value
		value = 0
	if cycle % 40 == X or (cycle % 40) - 1 == X or (cycle%40) - 2 == X:
		print("█", end="")
	else:
		print(".", end="")
	checkCycle(cycle)
	if line[0] == "a":
		command, value = line.split(" ")
		value = int(value)
		cycle += 1
		if cycle % 40 == X or (cycle % 40)+ 1 == X or (cycle%40)-1 == X:
			print("█", end="")
		else:
			print(".", end="")
		checkCycle(cycle)
	#	X += value
		
#print(sum)
