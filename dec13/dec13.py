import json

# input = open("example.txt").read().split("\n\n")
input = open("input.txt").read().split("\n\n")

def compareLists(left, right):
	if len(left) == 0:
		rightIndices.append(pairIndex)
	for i in range(len(left)):
		if i >= len(right):
			return False
		if type(right[i]) == list and type(left[i]) != list:
			left[i] = [left[i]]
		if type(left[i]) == list and type(right[i]) != list:
			right[i] = [right[i]]
		if (type(left[i]) != list): # integer checks
			if right[i] < left[i]:
				return False
			elif right[i] > left[i]:
				return True
			elif i == len(left) -1:
				return True
		else:
			return compareLists(left[i], right[i])

pairIndex = 0
rightIndices = []
for lines in input:
	if len(lines) < 1:
		break # empty line

	pairIndex += 1
	lines = lines.split("\n")
	left = json.loads(lines[0])
	right = json.loads(lines[1])
	i = 0
	
	if compareLists(left,right):
		rightIndices.append(pairIndex)
		
print(sum(rightIndices))