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

def check(x, y):
	for sens_x, sens_y, beac_x, beac_y in instructions:
		dist = get_manhattan_distance(sens_x, sens_y, beac_x, beac_y)
		check_dist = get_manhattan_distance(sens_x, sens_y, x, y)

		if (check_dist < dist):
			return False

	return True

for sens_x, sens_y, beac_x, beac_y in instructions:
	dist = get_manhattan_distance(sens_x, sens_y, beac_x, beac_y)
	for dist_x in range(dist+1):
		for i in range(4):
			dist_y = dist + 1 - dist_x
			x = sens_x + dist_x
			y = sens_y + dist_y
			if i % 2 == 1:
				x *= -1
			if i > 1:
				y *= -1

			if 0 <= x <= 4000000 and 0 <= y <= 4000000:
				if check(x, y):
					# total += 1
					print(x * 4000000 + y)
					exit()