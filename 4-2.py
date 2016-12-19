'''
--- Day 4: Security Through Obscurity ---
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

input: str
output: int
'''
import re

inFile = open("4.txt",'r')

sectorSum = 0
alpha = list("abcdefghijklmnopqrstuvwxyz")
lookup = {}
for bet in alpha:
	lookup[alpha.index(bet)] = bet

def getReal(name,offset):
	offset = offset%26
	words = name.split('-')
	realWords = []
	for word in words:
		newWord = []
		for letter in word:
			newLet = lookup[(alpha.index(letter)+offset)%26]
			newWord.append(newLet)
		realWords.append("".join(newWord))
	return(" ".join(realWords))

for line in inFile:
	wordHash = {}
	m = re.search("([a-z-]+)\-(\d+)\[(\w+)\]",line)
	word = m.group(1)
	sector = int(m.group(2))
	check = m.group(3)

	real = getReal(word,sector)
	if real == "northpole object storage":
		print("\""+real+"\" is in sector:",sector)