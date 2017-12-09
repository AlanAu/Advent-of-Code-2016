'''
--- Day 14: One-Time Pad ---

In order to communicate securely with Santa while you're on this mission, you've been using a one-time pad that you generate using a pre-agreed algorithm. Unfortunately, you've run out of keys in your one-time pad, and so you need to generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a pre-arranged salt (your puzzle input) and an increasing integer index (starting with 0, and represented in decimal); the resulting MD5 hash should be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

    It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
    One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

Considering future hashes for five-of-a-kind sequences does not cause those hashes to be skipped; instead, regardless of whether the current hash is a key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:

    The first index which produces a triple is 18, because the MD5 hash of abc18 contains ...cc38887a5.... However, index 18 does not count as a key for your one-time pad, because none of the next thousand hashes (index 19 through index 1018) contain 88888.
    The next index which produces a triple is 39; the hash of abc39 contains eee. It is also the first key: one of the next thousand hashes (the one at index 816) contains eeeee.
    None of the next six triples are keys, but the one after that, at index 92, is: it contains 999 and index 200 contains 99999.
    Eventually, index 22728 meets all of the criteria to generate the 64th key.

So, using our example salt of abc, index 22728 produces the 64th key.

Given the actual salt in your puzzle input, what index produces your 64th one-time pad key?
'''
import re
import hashlib

input = "cuanljph"
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
	while stretch < 1:
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