import sys
import os
import re

#one function takes a 1) "filename.in", writes a file to "filename.out"
#to the same directory as "filename.in" 2)filename.out is stripped of
# all whitespace line by line

## program without clearing comments

#extract filename and root from filename
if len(sys.argv) == 2:
	script, inputFilename = sys.argv
	rootName = os.path.splitext(inputFilename)[0]

	#create an output file in the same directory as input
	outputFile = open(rootName + ".out", 'w')

	#open input file 
	inputFile = open(inputFilename, 'r')


	#read each line of inputfile check if blank and skip it
	# else strip the line of 
	# spaces, tabs and write it to output file
	for line in inputFile:
		if line == "\n" or line == "\r":
			pass
		else:
			newLine = re.sub(r"[ \t\v]", "", line)
			outputFile.write(newLine)

	#close input and output files
	outputFile.close()
	inputFile.close()

##this control flow takes the same from above, but also strips
##comments out both inline and comments that take a whole line

elif len(sys.argv) == 3:
	if sys.argv[2] == "no-comments":

		script, inputFilename, commentsIndicator = sys.argv
		rootName = os.path.splitext(inputFilename)[0]

		#create an output file in the same directory as input
		outputFile = open(rootName + ".out", 'w')

		#open input file 
		inputFile = open(inputFilename, 'r')


		#read each line of inputfile check if blank and skip it
		# else strip the line of 
		# spaces, tabs and write it to output file
		for line in inputFile:

			if line.startswith("//"):
				pass

			elif "//" in line:
				line = line.partition('//')[0]
				line = line.rstrip()
				newLine = re.sub(r"[ \t\v]", "", line)
				outputFile.write(newLine)

			else:
				if line == "\n" or line == "\r":
					pass
				else:
					newLine = re.sub(r"[ \t\v]", "", line)
					outputFile.write(newLine)

		#close input and output files
		outputFile.close()
		inputFile.close()		

	else: 
		print("incorrect 3rd agrument, try 'no-comments' + \
			to strip comments or leave blank")

else:
	print ("incorrect number of arguments")