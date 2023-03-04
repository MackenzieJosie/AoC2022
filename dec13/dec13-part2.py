import json
from functools import cmp_to_key

# Opening file parsing the input
input = open("input.txt").read().replace("\n\n","\n").split("\n")

# recursive function to compare the left and right sides to determine if the inputs are in the right order
def compareLists(left, right):
	if len(left) == 0: # left list ran out of values, left is smaller
		return -1
	for i in range(len(left)):
		if i >= len(right): # left list is longer than right, right is smaller
			return 1
		# next two if statements make sure both values are lists if one is a list
		if type(right[i]) == list and type(left[i]) != list:
			left[i] = [left[i]]
		if type(left[i]) == list and type(right[i]) != list:
			right[i] = [right[i]]
		# neither are lists, check if integer values are the same
		if (type(left[i]) != list):
			if right[i] < left[i]:
				return 1 # right is smaller
			elif right[i] > left[i]:
				return -1 # left is smaller
			elif i == len(left) -1:
				return -1 # left ran out of values first, left is smaller
		else:
			return compareLists(left[i], right[i]) # both are lists, call itself to go inside lists for further comparison

	# left and right are the same
	return 0

# loads the packets from the input parsed with json.loads for ease
packets = []
for lines in input:
	if len(lines) < 1:
		break # empty line

	packets.append(json.loads(lines))

# part 2 required these two packets be added
packets.append([[6]])
packets.append([[2]])

# sort packets based off of compare function above
packets = sorted(packets, key=cmp_to_key(compareLists))

# find where the two decoder packets ended up
decoder = []
for i in range(len(packets)):
	if packets[i] == [[[[6]]]] or packets[i] == [[[[2]]]]:
		decoder.append(i+1)

# print solution
print(decoder[0], " * ", decoder[1], " = ", decoder[0]*decoder[1])