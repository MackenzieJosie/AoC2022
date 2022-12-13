input = open("input.txt").read().split("\n")
input.pop()
width, height = len(input[0]), len(input)

grid = [[0]*width for i in range(height)]
start = [0,0]
end = [0,0]

for i in range(len(input)):
	for j in range(len(input[i])):
		grid[i][j] = input[i][j]
		if input[i][j] == "S": start[0], start[1] = i, j
		elif input[i][j] == "E": end[0], end[1] = i, j

# part 1
queue = [[start]]
seen = [(start)]
while queue:
	path = queue.pop(0)
	x, y = path[-1]
	if grid[x][y] == "E":
		break
	for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
		if 0 <= x2 < height and 0 <= y2 < width and ((ord(grid[x2][y2]) - ord(grid[x][y])) < 2 or grid[x][y] == "S" ) and (x2, y2) not in seen:
			if (grid[x][y] != "z" and grid[x2][y2] == "E"):
				continue
			queue.append(path + [(x2,y2)])
			seen.append((x2,y2))

print("part 1:",len(path)-1)

# part 2
minPath = 999999999

for i in range(len(input)):
	for j in range(len(input[i])):
		if (grid[i][j] != "a"): continue
		start = i, j
		queue = [[start]]
		seen = [(start)]
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
					seen.append((x2,y2))

print("part 2:",minPath)