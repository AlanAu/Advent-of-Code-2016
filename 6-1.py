'''
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

input: str
output: str
'''
inFile = open("6.txt",'r')

msgHash = {}
message = []

for line in inFile:
	for index in range(len(line.strip())):
		letter = line[index]
		if index not in msgHash:
			msgHash[index] = {}
		if letter in msgHash[index]:
			msgHash[index][letter] += 1
		else:
			msgHash[index][letter] = 1

for index in range(len(msgHash)):
	message.append(sorted(msgHash[index],key=lambda x:msgHash[index][x],reverse=True)[0])
print ("Error-corrected message is:",''.join(message))