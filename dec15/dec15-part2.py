# Opening file and prepping for parsing the input
input = open("input.txt").read().replace("Sensor ","").replace(" closest beacon is ", "").replace("at ", "").replace(" ", "")
input = input.replace("x=","").replace("y=","").replace(":",",").split("\n")

# Parsing the instructions from the input
instructions = []
for line in input:
	if len(line) == 0:
		break
	line = line.split(",")
	instructions.append([int(line[0]),int(line[1]),int(line[2]),int(line[3])])

# Simple function to return manhattan distance from one coordinate to another
def get_manhattan_distance(x, y, x2, y2):
	return abs(x2 - x) + abs(y2 - y)

# Function to check with every instruction to see if the x, y values are in range of any beacons
def check(x, y):
	# loop through each instruction to check every beacon
	for sens_x, sens_y, beac_x, beac_y in instructions:
		# distance from beacon to sensor
		dist = get_manhattan_distance(sens_x, sens_y, beac_x, beac_y)
		# distance from coordinate to sensor
		check_dist = get_manhattan_distance(sens_x, sens_y, x, y)

		# if the checked distance is smaller than the distance, that means the coord is within range of beacon
		if (check_dist <= dist):
			return False

	# if the checked coordinate is out of range of all beacons, return true, this is the desired coordinate
	return True

# Main loop of program, loops through each instruction
for sens_x, sens_y, beac_x, beac_y in instructions:
	dist = get_manhattan_distance(sens_x, sens_y, beac_x, beac_y)
	# this nested loop checks the entire border of the range from the current sensor
	for dist_x in range(dist+1):
		for i in range(4):
			dist_y = dist + 1 - dist_x
			if i % 2 == 1:
				dist_y *= -1
			if i > 1:
				dist_x *= -1
					
			x = sens_x + dist_x
			y = sens_y + dist_y
		
			if dist_x == 0 and i > 1:
				x,y = y,x

			# uses check function on every coordinate bordering a range until finding the solution and stopping the program
			if 0 <= x <= 4000000 and 0 <= y <= 4000000:
				if check(x, y):
					print(x,y,x * 4000000 + y)
					exit()