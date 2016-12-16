'''
--- Day 7: Internet Protocol Version 7 ---
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

input: str
output: int
'''
import re

inFile = open("7.txt",'r')
#inFile = open("7b.txt",'r') #answer: 3
answer = 0

for address in inFile:
	address = address.strip()
	before = re.search(r"([a-z])(?!\1)([a-z])(\1)(?=[^\]]*\[).*\2\1\2(?=[^\[]*\])",address)
	after = re.search(r"([a-z])(?!\1)([a-z])(\1)(?=[^\[]*\]).*\][^\[]*\2\1\2",address)
	if before:
		answer += 1
	elif after:
		answer += 1
print("Number of IPs that support SSL:",answer)