'''
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
    rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
    rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did work, how many pixels should be lit?

input: str
output: int
'''
inFile = open("8.txt",'r')
#inFile = open("8a.txt",'r')

totalLit = 0
display = []
width = 50
height = 6
for _ in range(height):	display.append(list(map(int,list('0'*width))))

def rect(dim,display):
	col, row = list(map(int,dim.split('x')))
	for y in range(row):
		display[y][0:(col)] = list(map(int,list('1'*(col))))
		
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

for row in display:	totalLit += sum(row)
print("Number of lit pixels:",totalLit)