# Opening file and prepping for parsing the input
input = open("input.txt").read().split("\n")

walls = [] # list for storing lists of walls

max_x, min_x, max_y = 0, 500, 0
# grabbing instructions / parsing input
for line in input: # grabbing instructions / parsing input
	if len(line) < 1:
		break # empty line

	index = line.replace("-> ","").split(" ") # parsing into each separate coordinate in line
	wall = []
	# turning each index into an (x,y) as ints, also updates mins/maxes
	for lines in index:
		lines = lines.split(",")
		lines = [int(lines[0]),int(lines[1])]
		if lines[0] > max_x: max_x = lines[0]
		if lines[1] > max_y: max_y = lines[1]
		if lines[0] < min_x: min_x = lines[0]
		wall.append(lines)

	# appends list containing shape of current wall to list of all walls
	walls.append(wall)

# cave grid initialization
width = ((max_x - min_x) + 2)
height = max_y + 1
source = [0, 500-min_x]
cave = [["."] * width for i in range(height)]
cave[source[0]][source[1]] = "+"
# end of grid initialilzation

# function for drawing the walls on grid between to points
def draw_line(point_1, point_2):
	cave[point_1[1]][point_1[0]-min_x] = "#"
	while point_1 != point_2:
		if point_1[0] < point_2[0]:
			point_1[0] += 1
		if point_1[0] > point_2[0]:
			point_1[0] -= 1
		if point_1[1] < point_2[1]:
			point_1[1] += 1
		if point_1[1] > point_2[1]:
			point_1[1] -= 1
		cave[point_1[1]][point_1[0]-min_x] = "#"
	
# loop through walls list to draw all walls parsed from input
for wall in walls: # drawing walls
	for i in range(len(wall)-1):
		draw_line(wall[i], wall[i+1])


# function for pouring the sand into the grid from the source
def pour_sand(source):
	unit = [source[0] + 1, source[1]]
	while cave[unit[0]][unit[1]] == ".":
		unit[0] += 1
		if unit[0] > max_y:
			return False
		if cave[unit[0]][unit[1]] != ".":
			if cave[unit[0]][unit[1]-1] == ".":
				unit[1] -= 1
			elif cave[unit[0]][unit[1]+1] == ".":
				unit[1] += 1
	cave[unit[0]-1][unit[1]] = "o"
	return True

# loop to pour sand until no more sand can be poured, keeping track of total amount of sand poured
sand_count = 0
while pour_sand(source):
	sand_count += 1

print(sand_count) # printing solution

# can also use this to print the result of the grid to look at result or debug
# for line in cave: # printing cave
# 	print(line)