'''
--- Day 3: Squares With Three Sides ---
--- Part Two ---
Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

input: str
output: int
'''
inFile = open("3.txt",'r') #format is 3 space-separated integers on each line
triangles = 0
first = inFile.readline().strip()

def isTri(a,b,c):
	if a>0 and b>0 and c>0:
		if a+b>c and a+c>b and b+c>a:
			return 1
	return 0

while len(first)>0:
	a1,b1,c1 = list(map(int,first.split()))
	a2,b2,c2 = list(map(int,inFile.readline().split()))
	a3,b3,c3 = list(map(int,inFile.readline().split()))
	first = inFile.readline().strip()

	triangles += isTri(a1,a2,a3)
	triangles += isTri(b1,b2,b3)
	triangles += isTri(c1,c2,c3)
print("Total number of valid triangles:",triangles)