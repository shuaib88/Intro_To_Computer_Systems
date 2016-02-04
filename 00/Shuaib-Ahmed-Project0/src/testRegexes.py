import sys
import os
import re

#create an output file in the same directory as input
outputFile = open ("testFile.out", 'w')

#open input file 
inputFile = open("testFile.in", 'r')


# pattern objects
# match ab
ab = re.compile('@')

for line in inputFile:
	if result == ab.match(line):
		print (result)


