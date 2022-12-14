import json
from functools import cmp_to_key

# input = open("example.txt").read().split("\n\n")
input = open("input.txt").read().replace("\n\n","\n").split("\n")

def compareLists(left, right):
	if len(left) == 0:
		return -1
	for i in range(len(left)):
		if i >= len(right):
			return 1
		if type(right[i]) == list and type(left[i]) != list:
			left[i] = [left[i]]
		if type(left[i]) == list and type(right[i]) != list:
			right[i] = [right[i]]
		if (type(left[i]) != list): # integer checks
			if right[i] < left[i]:
				return 1
			elif right[i] > left[i]:
				return -1
			elif i == len(left) -1:
				return -1
		else:
			return compareLists(left[i], right[i])

	return 0

packets = []
for lines in input:
	if len(lines) < 1:
		break # empty line

	packets.append(json.loads(lines))

packets.append([[6]])
packets.append([[2]])

packets = sorted(packets, key=cmp_to_key(compareLists))

decoder = []
for i in range(len(packets)):
	if packets[i] == [[[[6]]]] or packets[i] == [[[[2]]]]:
		decoder.append(i+1)

print(decoder[0]*decoder[1])