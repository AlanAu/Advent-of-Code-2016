'''
--- Part Two ---

What do you get if you multiply together the values of one chip in each of outputs 0, 1, and 2?

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
			#if lowVal == lChip and highVal == hChip:
			#	print("Number of the bot which compares chips",highVal,"and",lowVal,"is:",target.split()[1])
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

out0 = int(botValues["output 0"][0])
out1 = int(botValues["output 1"][0])
out2 = int(botValues["output 2"][0])
print("The product of outputs 0, 1, and 2 is:",out0*out1*out2)