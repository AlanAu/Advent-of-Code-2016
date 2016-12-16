'''
--- Day 12: Leonardo's Monorail ---
--- Part Two ---

As you head down the fire escape to the monorail, you notice it didn't start; register c needs to be initialized to the position of the ignition key.

If you instead initialize register c to be 1, what value is now left in register a?

input: str
output: str
'''
inFile = open("12.txt",'r')
#inFile = open("12a.txt",'r') #output: 42

regs = ['a','b','c','d']
register = {'a':0,'b':0,'c':1,'d':0}
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
