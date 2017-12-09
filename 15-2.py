'''
--- Day 15: Timing is Everything ---
--- Part Two ---

After getting the first capsule (it contained a star! what great fortune!), the machine detects your success and begins to rearrange itself.

When it's done, the discs are back in their original configuration as if it were time=0 again, but a new disc with 11 positions and starting at position 0 has appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the configuration in your puzzle input, what is the first time you can press the button to get another capsule?

Your puzzle input:
Disc #1 has 17 positions; at time=0, it is at position 1.
Disc #2 has 7 positions; at time=0, it is at position 0.
Disc #3 has 19 positions; at time=0, it is at position 2.
Disc #4 has 5 positions; at time=0, it is at position 0.
Disc #5 has 3 positions; at time=0, it is at position 0.
Disc #6 has 13 positions; at time=0, it is at position 5. 
Disc #7 has 11 positions; at time=0, it is at position 0. 
(Part Two)
'''
time = 0
disc = [17,7,19,5,3,13,11]
now = [1,0,2,0,0,5,0]
solved = 0

while solved == 0:
	fail = 0
	i = 0
	while i < len(disc):
		if (now[i]+time+i+1)%disc[i]!=0:
			fail = 1
			i = len(disc)
		i += 1
	if fail == 0:
		solved = 1
		continue
	time += 1

print("The first time you can press the button to get a capsule is:",time)