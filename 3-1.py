'''
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

input: str
output: int
'''
inFile = open("3.txt",'r') #format is 3 space-separated integers on each line
triangles = 0

for _ in inFile:
	a,b,c = list(map(int,_.split()))
	if a>0 and b>0 and c>0:
		if a+b>c and b+c>a and a+c>b:
			triangles += 1
print("Total number of valid triangles:",triangles)