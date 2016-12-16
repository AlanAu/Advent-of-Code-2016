'''
--- Day 1: No Time for a Taxicab ---
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

input: list(str)
output: int
'''
inFile = open("1.txt",'r')
input = inFile.read().split(', ')
lastDir = 'N'
xCoord = 0
yCoord = 0
visited = {0:{0:1}}
found = 0

def getDir(turn,last):
	direction = ['N','E','S','W']
	if turn == 'R':
		newIndex = direction.index(last) + 1
		if newIndex > 3: newIndex -= 4
	else:
		newIndex = direction.index(last) - 1
		if newIndex < 0: newIndex += 4
	return direction[newIndex]

for step in input:
	newDir = getDir(step[0],lastDir)
	lastDir = newDir
	stepSize = int(step[1:])
	if newDir == 'N':
		for trackY in range(yCoord+1,yCoord+stepSize+1):
			if trackY in visited[xCoord]:
				found = 1
				break
			else:
				visited[xCoord][trackY] = 1
		yCoord = trackY
	elif newDir == 'S':
		for trackY in range(yCoord-1,yCoord-stepSize-1,-1):
			if trackY in visited[xCoord]:
				found = 1
				break
			else:
				visited[xCoord][trackY] = 1
		yCoord = trackY
	elif newDir == 'E':
		for trackX in range(xCoord+1,xCoord+stepSize+1):
			if trackX not in visited:
				visited[trackX] = {}
			if yCoord in visited[trackX]:
				found = 1
				break
			else:
				visited[trackX][yCoord] = 1
		xCoord = trackX
	else:
		for trackX in range(xCoord-1,xCoord-stepSize-1,-1):
			if trackX not in visited:
				visited[trackX] = {}
			if yCoord in visited[trackX]:
				found = 1
				break
			else:
				visited[trackX][yCoord] = 1
		xCoord = trackX
	if found == 1:
		xDist = abs(xCoord)
		yDist = abs(yCoord)
		print("Total distance to repeat location is:",xDist+yDist)
		exit()
