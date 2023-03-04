import json

# Opening file parsing the input
input = open("input.txt").read().split("\n\n")

# recursive function to compare the left and right sides to determine if the inputs are in the right order
def compareLists(left, right):
	if len(left) == 0: # left list ran out of values, left is smaller
		return True
	for i in range(len(left)): 
		if i >= len(right): # left list is longer than right, right is smaller
			return False
		# next two if statements make sure both values are lists if one is a list
		if type(right[i]) == list and type(left[i]) != list:
			left[i] = [left[i]]
		if type(left[i]) == list and type(right[i]) != list:
			right[i] = [right[i]]
		# neither are lists, check if integer values are the same
		if (type(left[i]) != list):
			if right[i] < left[i]:
				return False # right is smaller
			elif right[i] > left[i]:
				return True # left is smaller
			elif i == len(left) -1:
				return True # left list is shorter than right list, left is smaller
		else:
			return compareLists(left[i], right[i]) # both are lists, call itself to go inside lists for further comparison

# main loop to keep track of which and how many pairs are right
pairIndex = 0
rightIndices = []
for lines in input:
	if len(lines) < 1:
		break # empty line

	pairIndex += 1

	# parsing the pair into left and right
	lines = lines.split("\n")
	left = json.loads(lines[0])
	right = json.loads(lines[1])
	
	# using function to compare and determine if the pair is in the right order
	if compareLists(left,right):
		rightIndices.append(pairIndex)
		
# prints solution
print(sum(rightIndices))