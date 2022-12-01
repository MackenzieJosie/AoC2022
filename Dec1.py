def main():
	max = 0
	sum = 0
	with open("input.txt") as input_file:
		#data = input_file.read()
		for line in input_file:
			if (len(line) > 1):
				sum = sum + int(line)
			else:
				if (sum > max):
					max = sum
				sum = 0
	print(max)

#Call the main function
main()
