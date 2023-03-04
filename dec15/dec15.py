# Opening file and prepping for parsing the input
input = open("input.txt").read().replace("Sensor ","").replace(" closest beacon is ", "").replace("at ", "").replace(" ", "")
input = input.replace("x=","").replace("y=","").replace(":",",").split("\n")

# Parsing the instructions from the input
instructions = []
for line in input:
	if len(line) == 0:
		break
	line = line.split(",")
	instructions.append([int(line[0]),int(line[1]),int(line[2]),int(line[3])]) # each instruction is stored as [x,y,x2,y2] where x, y is the sensor and x2, y2 is the closest beacon to that sensor


# Simple function to return manhattan distance from one coordinate to another
def get_manhattan_distance(x, y, x2, y2):
	return abs(x2 - x) + abs(y2 - y)

# Function for drawing out #'s where there cannot be a beacon
def draw_area(x, y, x2, y2):
	# man_dist is the distance from the sensor to the beacon
	man_dist = get_manhattan_distance(x,y,x2,y2)
	local_sum = 0
	i = 0
	# bottom_y is the bottom row of the diamond shape
	bottom_y = y + man_dist
	# this loop is to go through all the y values within the manhattan distance of the sensor, to draw the shape as shown in problem description
	for top_y in range(y-man_dist, y):
		# for this problem, the only row in the grid that matters is the TARGET_Y, so that is the only row we apply the function to
		if top_y == TARGET_Y or bottom_y == TARGET_Y:
			# this loops through all the x values that would be drawn
			for new_x in range(x-i, x + i + 1):
				# these conditions are for checking if the current y value is the target, and if the value has been drawn or not
				# if the y value is the target, and the value is new, the local sum is incremented
				if top_y == TARGET_Y:
					if new_x not in area[top_y]:
						area[top_y][new_x] = "#"
						local_sum += 1
				if bottom_y == TARGET_Y:
					if new_x not in area[bottom_y]:
						area[bottom_y][new_x] = "#"
						local_sum += 1
		bottom_y -= 1
		i += 1

	# same as above except for the row of the sensor
	if y == TARGET_Y:
		for new_x in range(x-man_dist, x + man_dist):
			if new_x not in area[y]:
				area[y][new_x] = "#"
				local_sum += 1
	
	# drawing where the sensor/beacon are if they are on the Target Y
	if y == TARGET_Y:
		area[y][x] = "S"
	if y2 == TARGET_Y:
		area[y2][x2] = "B"

	# return the amount of #'s that were drawn from the current instruction
	return local_sum

# initializing the target y value, as well as a dict of dicts to keep track of the grid
area = {}
TARGET_Y = 2000000

area[TARGET_Y] = {}

# main loop for problem solution, adds the local sums from each instruction to the total sum
sum = 0
for instruction in instructions:
	sum += draw_area(instruction[0],instruction[1],instruction[2],instruction[3])

# print solution
print(sum)