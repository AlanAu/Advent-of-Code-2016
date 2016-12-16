'''
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?

input: str
output: int
'''
import re

inFile = open("7.txt",'r')
#inFile = open("7a.txt",'r')
answer = 0

for address in inFile:
	address = address.strip()
	nope = re.search(r"\[[^\]]*(.)(?!\1)(.)(\2)(\1)[^\[]*\]",address)
	yup = re.search(r"(.)(?!\1)(.)(\2)(\1)",address)
	if nope:
		continue
	elif yup:
		answer += 1
print("Number of IPs that support TLS:",answer)