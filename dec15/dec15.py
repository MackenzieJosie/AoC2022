# input = open("example.txt").read().split("\n")
input = open("input.txt").read().replace("Sensor ","").replace(" closest beacon is ", "").replace("at ", "").replace(" ", "")
input = input.replace("x=","").replace("y=","").replace(":",",").split("\n")

instructions = []
for line in input:
	if len(line) == 0:
		break
	line = line.split(",")
	# print(line)
	instructions.append([int(line[0]),int(line[1]),int(line[2]),int(line[3])])

def get_manhattan_distance(x, y, x2, y2):
	return abs(x2 - x) + abs(y2 - y)

area = {}
TARGET_Y = 2000000

area[TARGET_Y] = {}
def draw_area(x, y, x2, y2):
	man_dist = get_manhattan_distance(x,y,x2,y2)
	local_sum = 0
	i = 0
	bottom_y = y + man_dist
	for top_y in range(y-man_dist, y):
		# if top_y not in area and top_y == TARGET_Y:
		# 	area[top_y] = {}
		# if bottom_y not in area and bottom_y == TARGET_Y:
		# 	area[bottom_y] = {}

		if top_y == TARGET_Y or bottom_y == TARGET_Y:
			for new_x in range(x-i, x + i + 1):
				if top_y == TARGET_Y:
					if new_x not in area[top_y]:
						area[top_y][new_x] = "#"
						local_sum += 1
				if bottom_y == TARGET_Y:
					if new_x not in area[bottom_y]:
						area[bottom_y][new_x] = "#"
						local_sum += 1
		# 	print(new_x, end=" ")
		# print()
		# print(i,top_y, bottom_y)
		bottom_y -= 1
		i += 1
	# if y not in area:
	# 	area[y] = {}
	if y == TARGET_Y:
		for new_x in range(x-man_dist, x + man_dist):
			if new_x not in area[y]:
				area[y][new_x] = "#"
				local_sum += 1
	
	if y == TARGET_Y:
		area[y][x] = "S"
	if y2 == TARGET_Y:
		area[y2][x2] = "B"

	return local_sum

sum = 0
for instruction in instructions:
	sum += draw_area(instruction[0],instruction[1],instruction[2],instruction[3])


print(sum)