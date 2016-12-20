'''
--- Day 20: Firewall Rules ---
--- Part Two ---

How many IPs are allowed by the blacklist?

'''
inFile = open("20.txt",'r')
lowest = 0
highest = 4294967295
count = 0
blockHash = {}
for line in inFile:
	low,high = list(map(int,line.split('-')))
	blockHash[low] = high

for low in sorted(blockHash):
	if low > lowest:
		count += low - lowest
	if blockHash[low] > lowest:
		lowest = blockHash[low]+1

lowest = min(lowest,highest)
count += highest - lowest
print ("Number of valid IP address is:",count)