'''
--- Day 2: Bathroom Security ---
--- Part Two ---

You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD

You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

    You start at "5" and don't move at all (up and left are both edges), ending at 5.
    Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
    Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
    Finally, after five more moves, you end at 3.

So, given the actual keypad layout, the code would be 5DB3.

Using the same instructions in your puzzle input, what is the correct bathroom code?

input: str
output: str
'''
inFile = open("2.txt",'r')
input = inFile.readlines()
numpad = [['0','0','1','0','0'],['0','2','3','4','0'],['5','6','7','8','9'],['0','A','B','C','0'],['0','0','D','0','0']]
bathCode = ""
#initial row and col
row = 2
col = 0

def newDigit(startPos,command):
	row = startPos[0]
	col = startPos[1]
	output = []
	for direction in command:
		if direction == 'U':
			if (row-1) < 0: continue #hard boundary
			elif numpad[row-1][col] == '0': continue #soft boundary
			else: row -= 1
		if direction == 'D':
			if (row+1) > 4: continue
			elif numpad[row+1][col] == '0': continue
			else: row += 1
		if direction == 'L':
			if (col-1) < 0: continue
			elif numpad[row][col-1] == '0': continue
			else: col -= 1
		if direction == 'R':
			if (col+1) > 4: continue
			elif numpad[row][col+1] == '0': continue
			else: col += 1
	output.append(row)
	output.append(col)
	return(output)

for digit in input:
	row,col = newDigit([row,col],digit)
	bathCode+=(numpad[row][col])

print("Bathroom code is:",bathCode)