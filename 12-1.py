'''
--- Day 12: Leonardo's Monorail ---

You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt some of the files you extracted from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's assembunny code designed for the new computer you just assembled. You'll have to execute the code and get the password.

The assembunny code you've extracted operates on four registers (a, b, c, and d) that start at 0 and can hold any integer. However, it seems to make use of only a few instructions:

    cpy x y copies x (either an integer or the value of a register) into register y.
    inc x increases the value of register x by one.
    dec x decreases the value of register x by one.
    jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.

The jnz instruction moves relative to itself: an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

For example:

cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a

The above code would set register a to 41, increase its value by 2, decrease its value by 1, and then skip the last dec a (because a is not zero, so the jnz a 2 skips it), leaving register a at 42. When you move past the last instruction, the program halts.

After executing the assembunny code in your puzzle input, what value is left in register a?

input: str
output: str
'''
inFile = open("12.txt",'r')
#inFile = open("12a.txt",'r') #output: 42

regs = ['a','b','c','d']
register = {'a':0,'b':0,'c':0,'d':0}
skip = 0

def cpy(x,y):
	if x in regs:
		register[y] = register[x]
	else:
		register[y] = int(x)

def inc(x):
	value = register[x]
	value += 1
	register[x] = value

def dec(x):
	value = register[x]
	value -= 1
	register[x] = value

def jnz(x,y):
	jump = 1
	if x in regs:
		if register[x] != 0:
			jump = int(y)
	elif int(x) != 0:
		jump = int(y)
	return (jump)
	
instructions = []	
for line in inFile:
	instructions.append(line.strip().split())

index = 0
while index < len(instructions):	
	inst = instructions[index]
	cmd = inst[0]
	if cmd == 'cpy':
		cpy(inst[1],inst[2])
	elif cmd == 'inc':
		inc(inst[1])
	elif cmd == 'dec':
		dec(inst[1])
	elif cmd == 'jnz':
		index += jnz(inst[1],inst[2])
		continue
	index += 1
	
print("The final value in register \'a\' is:",register['a'])
