#by jasmine
#february 2017
#v 0.0.1

#import libraries
import sys
import random

all_lines = list()
# all_lines = []

for line in sys.stdin:
	line = line.strip()
	if "(" in line:
		#this makes firstw the full element name
		pos = line.find(" ")
		element = line[:pos]
		secondw = line[pos+1:]
		#and thirdw the short el & no.
		elmno = secondw[3:]
		ium = line[3:pos]
		#first 3 will always be the last element in the loop
		#which is not fun
		first3 = line[:3]
		newline = element 
	else:
		if "ses" in line:
			newline = line.replace("ses", ium)
		elif "ex" in line:
			pos = line.find(" ")
			product1 = line[:pos]
			product2 = line[pos+1:]
			newline = product1 + " " + first3 + product2 + ium
		else:
			newline = line + ium

	all_lines.append(newline)
	random.shuffle(all_lines)

for line in all_lines:
	print line