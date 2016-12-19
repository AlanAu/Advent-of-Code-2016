'''
--- Day 8: Two-Factor Authentication ---
--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

input: str
output: str
'''
inFile = open("8.txt",'r')
#inFile = open("8a.txt",'r')

totalLit = 0
display = []
width = 50
height = 6
for _ in range(height):	display.append(list(' '*width))

def rect(dim,display):
	col, row = list(map(int,dim.split('x')))
	for y in range(row):
		display[y][0:(col)] = list('*'*(col))
		
def rotateRow(whichRow,shift,display):
	row = int(whichRow.split('=')[1])
	offset = -(int(shift)%width)
	oldRow = display[row]
	newRow = []
	newRow.extend(oldRow[offset:])
	newRow.extend(oldRow[:offset])
	display[row] = newRow

def rotateColumn(whichCol,shift,display):
	col = int(whichCol.split('=')[1])
	offset = -(int(shift)%height)
	oldCol = []
	for row in display:
		oldCol.append(row[col])
	newCol = []
	newCol.extend(oldCol[offset:])
	newCol.extend(oldCol[:offset])
	for index in range(len(display)):
		display[index][col] = newCol[index]
	
for line in inFile:
	command = line.split()
	if command[0] == 'rect':
		rect(command[1],display)
	elif command[0] == 'rotate':
		if command[1] == 'row':
			rotateRow(command[2],command[4],display)
		elif command[1] == 'column':
			rotateColumn(command[2],command[4],display)

for row in display:
	print(''.join(map(str,row)))