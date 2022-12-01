def main():
	max = []
	sum = 0
	with open("input.txt") as input_file:
		for line in input_file:
			if (len(line) > 1):
				sum = sum + int(line)
			else:	
				max.append(sum)
				sum = 0
		max.append(sum) # for the end of file
	max.sort(reverse = True)
	print(max[0])
	print(max[0]+max[1]+max[2])

main()
