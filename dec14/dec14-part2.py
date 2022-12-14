# input = open("example.txt").read().split("\n")
input = open("input.txt").read().split("\n")

walls = []

max_x, min_x, max_y = 0, 500, 0
for line in input: # grabbing instructions / parsing input
	if len(line) < 1:
		break # empty line

	row = line.replace("-> ","").split(" ")
	wall = []
	for lines in row:
		lines = lines.split(",")
		lines = [int(lines[0]),int(lines[1])]
		if lines[0] > max_x: max_x = lines[0]
		if lines[1] > max_y: max_y = lines[1]
		if lines[0] < min_x: min_x = lines[0]
		wall.append(lines)

	walls.append(wall)

# cave grid initialization
width = (max_x*2)
height = max_y + 3
source = [0, 500]
cave = [["."] * width for i in range(height)]

for i in range(width):
	cave[height-1][i] = "#"

cave[source[0]][source[1]] = "+"

def draw_line(point_1, point_2):
	cave[point_1[1]][point_1[0]] = "#"
	while point_1 != point_2:
		if point_1[0] < point_2[0]:
			point_1[0] += 1
		if point_1[0] > point_2[0]:
			point_1[0] -= 1
		if point_1[1] < point_2[1]:
			point_1[1] += 1
		if point_1[1] > point_2[1]:
			point_1[1] -= 1
		cave[point_1[1]][point_1[0]] = "#"
	
for wall in walls: # drawing walls
	for i in range(len(wall)-1):
		draw_line(wall[i], wall[i+1])


def pour_sand(source):
	unit = [source[0], source[1]]
	while cave[unit[0]][unit[1]] == "." or cave[unit[0]][unit[1]] == "+":
		unit[0] += 1
		if cave[unit[0]][unit[1]] != ".":
			if cave[unit[0]][unit[1]-1] == ".":
				unit[1] -= 1
			elif cave[unit[0]][unit[1]+1] == ".":
				unit[1] += 1
	if cave[unit[0]-1][unit[1]] == "+":
		return False
	cave[unit[0]-1][unit[1]] = "o"
	return True

sand_count = 0
while pour_sand(source):
	sand_count += 1

# for line in cave: # printing cave to check
# 	print(line)
print(sand_count + 1)