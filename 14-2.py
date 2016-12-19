'''
--- Day 14: One-Time Pad ---
--- Part Two ---

Of course, in order to make this process even more secure, you've also implemented key stretching.

Key stretching forces attackers to spend more time generating hashes. Unfortunately, it forces everyone else to spend more time, too.

To implement key stretching, whenever you generate a hash, before you use it, you first find the MD5 hash of that hash, then the MD5 hash of that hash, and so on, a total of 2016 additional hashings. Always use lowercase hexadecimal representations of hashes.

For example, to find the stretched hash for index 0 and salt abc:

    Find the MD5 hash of abc0: 577571be4de9dcce85a041ba0410f29f.
    Then, find the MD5 hash of that hash: eec80a0c92dc8a0777c619d9bb51e910.
    Then, find the MD5 hash of that hash: 16062ce768787384c81fe17a7a60c7e3.
    ...repeat many times...
    Then, find the MD5 hash of that hash: a107ff634856bb300138cac6568c0f24.

So, the stretched hash for index 0 in this situation is a107ff.... In the end, you find the original hash (one use of MD5), then find the hash-of-the-previous-hash 2016 times, for a total of 2017 uses of MD5.

The rest of the process remains the same, but now the keys are entirely different. Again for salt abc:

    The first triple (222, at index 5) has no matching 22222 in the next thousand hashes.
    The second triple (eee, at index 10) hash a matching eeeee at index 89, and so it is the first key.
    Eventually, index 22551 produces the 64th key (triple fff with matching fffff at index 22859.

Given the actual salt in your puzzle input and using 2016 extra MD5 calls of key stretching, what index now produces your 64th one-time pad key?

Your puzzle input is still ahsbgdzn.
'''
import re
import hashlib

input = "ahsbgdzn"
#input = "abc" #test input, output should be: 22551

total = 64
index = 0
last5 = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'a':0,'b':0,'c':0,'d':0,'e':0,'f':0}
hashCount = 0
fiveCount = 0
m3Hash = {}
goodList = []

def getMD5(hashStr):
	stretch = 0
	while stretch < 2017:
		m = hashlib.md5()
		m.update(hashStr.encode('utf-8'))
		hashStr = (m.hexdigest())
		stretch += 1
	return(hashStr)

def getCount(low,high,key):
	count = 0
	for i in range(low,high):
		if i in m3Hash[key]:
			goodList.append(i)
			count += 1
	return(count)

while hashCount < total:
	inHash = getMD5(input+str(index))
	m3 = re.search(r"(.)\1\1",inHash)
	m5 = re.search(r"(.)\1\1\1\1",inHash)
	if m3:
		if m3.group(1) not in m3Hash:
			m3Hash[m3.group(1)] = []
		m3Hash[m3.group(1)].append(index)
	if m5:
		hashCount += getCount(max(index-1000,last5[m5.group(1)]),index-1,m5.group(1))
		last5[m5.group(1)] = index
	index += 1

print("Key number",total,"is at index:",goodList[total-1])