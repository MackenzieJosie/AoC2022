# Opening file parsing the input
input = open("input.txt").read().split("\n")
input.pop() # discarding empty last line from parsing
width, height = len(input[0]), len(input) # storing the height and width of the input grid

# drawing out the input file onto a 2D List as well as finding and storing the Start coordinates
grid = [[0]*width for i in range(height)]

for i in range(len(input)):
	for j in range(len(input[i])):
		grid[i][j] = input[i][j]
		if input[i][j] == "S": start = i, j

# part 1
# this is a basic implementation of dijkstra's algorithm
queue = [[start]]
seen = set([(start)])
while queue:
	path = queue.pop(0)
	x, y = path[-1]
	if grid[x][y] == "E":
		break # made it to the end! can leave loop

	# looping through all possible directions to travel
	for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
		# checks if coordinates are a valid location to travel to
		if 0 <= x2 < height and 0 <= y2 < width and ((ord(grid[x2][y2]) - ord(grid[x][y])) < 2 or grid[x][y] == "S" ) and (x2, y2) not in seen:
			if (grid[x][y] != "z" and grid[x2][y2] == "E"):
				continue # back to the next in queue, can only go from z to E to end
			queue.append(path + [(x2,y2)])
			seen.add((x2,y2))

print("part 1:",len(path)-1)

# part 2
minPath = 999999999

# looping through entire grid checking dijkstra's shortest path on all points that have the value 'a' and keeping track of the shortest path of them
for i in range(len(input)):
	for j in range(len(input[i])):
		if (grid[i][j] != "a"): continue
		start = i, j
		# below this is same dijkstra's algorithm implementation as part 1 above
		queue = [[start]]
		seen = set([(start)])
		while queue:
			path = queue.pop(0)
			x, y = path[-1]
			if grid[x][y] == "E":
				if len(path)-1 < minPath:
					minPath = len(path) -1
				break
			for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
				if 0 <= x2 < height and 0 <= y2 < width and ((ord(grid[x2][y2]) - ord(grid[x][y])) < 2 or grid[x][y] == "S" ) and (x2, y2) not in seen:
					if (grid[x][y] != "z" and grid[x2][y2] == "E"):
						continue
					queue.append(path + [(x2,y2)])
					seen.add((x2,y2))

print("part 2:",minPath)