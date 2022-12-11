input = open("input.txt").read().split("\n")
input.pop()

cycle = 0
X = 1
sum = 0
value = 0

def checkCycle(number):
	if number == 20 or ((number - 20) % 40) == 0:
		print(number, X)
		return number * X
	return 0

for line in input:
	#sum += checkCycle(cycle)
	cycle += 1
	if value:
		X+= value
		value = 0
	sum += checkCycle(cycle)
	if line[0] == "a":
		command, value = line.split(" ")
		value = int(value)
		cycle += 1
		sum += checkCycle(cycle)
	#	X += value
		
print(sum)