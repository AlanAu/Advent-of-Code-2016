'''
--- Day 6: Signals and Noise ---
--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

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
	message.append(sorted(msgHash[index],key=lambda x:msgHash[index][x])[0])
print ("Error-corrected message is:",''.join(message))