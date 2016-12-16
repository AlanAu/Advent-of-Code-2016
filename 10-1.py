'''
--- Day 10: Balance botValues ---

You come upon a factory in which many robots are zooming around handing small microchips to each other.

Upon closer examination, you notice that each bot only proceeds when it has two microchips, and once it does, it gives each one to a different bot or puts it in a marked "output" bin. Sometimes, botValues take microchips from "input" bins, too.

Inspecting one of the microchips, it seems like they each contain a single number; the botValues must use some logic to decide what to do with each chip. You access the local control computer and download the botValues' instructions (your puzzle input).

Some of the instructions specify that a specific-valued microchip should be given to a specific bot; the rest of the instructions indicate what a given bot should do with its lower-value or higher-value chip.

For example, consider the following instructions:

value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2

    Initially, bot 1 starts with a value-3 chip, and bot 2 starts with a value-2 chip and a value-5 chip.
    Because bot 2 has two microchips, it gives its lower one (2) to bot 1 and its higher one (5) to bot 0.
    Then, bot 1 has two microchips; it puts the value-2 chip in output 1 and gives the value-3 chip to bot 0.
    Finally, bot 0 has two microchips; it puts the 3 in output 2 and the 5 in output 0.

In the end, output bin 0 contains a value-5 microchip, output bin 1 contains a value-2 microchip, and output bin 2 contains a value-3 microchip. In this configuration, bot number 2 is responsible for comparing value-5 microchips with value-2 microchips.

Based on your instructions, what is the number of the bot that is responsible for comparing value-61 microchips with value-17 microchips?

input: str
output: int
'''

inFile = open("10.txt",'r')
valFile = open("10.txt",'r')
#inFile = open("10a.txt",'r')
#valFile = open("10a.txt",'r')

lChip = '17'
hChip = '61'
#lChip = 2
#hChip = 5

botValues = {}
instructions = {}

def activate(target,value):
	if target not in botValues:
		botValues[target] = [value]
	else:
		botValues[target].append(value)
		if len(botValues[target]) > 1:
			lowBot = instructions[target][0]
			highBot = instructions[target][1]
			lowVal, highVal = sorted(botValues[target],key=lambda x:int(x))
			botValues[target] = []
			if lowVal == lChip and highVal == hChip:
				print("Number of the bot which compares chips",highVal,"and",lowVal,"is:",target.split()[1])
			activate(lowBot,lowVal)
			activate(highBot,highVal)

for _ in inFile:
	inst = _.split()
	if inst[0] == "bot":
		active = " ".join([inst[0],inst[1]])
		low = " ".join([inst[5],inst[6]])
		high = " ".join([inst[10],inst[11]])
		instructions[active] = [low,high]
for _ in valFile:
	inst = _.split()
	if inst[0] == "value":
		value = inst[1]
		target = " ".join([inst[4],inst[5]])
		activate(target,value)