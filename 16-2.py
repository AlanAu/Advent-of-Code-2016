'''
--- Day 16: Dragon Checksum ---
--- Part Two ---

The second disk you have to fill has length 35651584. Again using the initial state in your puzzle input, what is the correct checksum for this disk?

Your puzzle input is still 11100010111110100.
'''
original = list('11100010111110100')
input = list(original)
disk = 35651584
output = []

def oneComp(x):
	out = []
	for i in x:
		if i == '0':
			out.append('1')
		else:
			out.append('0')
	return(out)

def getCheck(input):
	check = []
	if len(input)%2==1:
		return(input)
	for i in range(0,len(input),2):
		x = input[i]
		y = input[i+1]
		if x == y:
			check.append('1')
		else:
			check.append('0')
	if len(check)%2 == 0:
		check = getCheck(check)
	return(check)
	
while len(input) < disk:
	inCopy = list(input)
	inCopy.reverse()
	inCopy = oneComp(inCopy)
	input.extend('0')
	input.extend(inCopy)
	
input = input[:disk]
output = getCheck(input)

print("The correct checksum for",''.join(original),"is:",''.join(output))