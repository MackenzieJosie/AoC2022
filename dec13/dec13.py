import json

# input = open("example.txt").read().split("\n\n")
input = open("input.txt").read().split("\n\n")

def compareLists(left, right):
	if len(left) == 0:
		# print(pairIndex, "is right")
		rightIndices.append(pairIndex)
	for i in range(len(left)):
		if i >= len(right):
			# print(pairIndex, "right list ran out so wrong")
			return False
		if type(right[i]) == list and type(left[i]) != list:
			left[i] = [left[i]]
		if type(left[i]) == list and type(right[i]) != list:
			right[i] = [right[i]]
		# print(left[i], right[i])
		if (type(left[i]) != list): # integer checks
			if right[i] < left[i]:
				# print(pairIndex, "right is smaller so wrong")
				return False
			elif right[i] > left[i]:
				# print(pairIndex, "left is smaller so right")
				return True
			elif i == len(left) -1:
				# print(pairIndex, "left list ran out so right")
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
	
	# print(left, len(left), ":", right, len(right))

	if compareLists(left,right):
		rightIndices.append(pairIndex)
		
print(sum(rightIndices))