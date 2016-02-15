import sys

import os

from Parser import Parser

from RemoveWhitespace import RemoveWhitespace

#extract filename and root from filename
script, inputFilename = sys.argv
rootName = os.path.splitext(inputFilename)[0]
print(rootName)

#declare output file path
outFile = rootName + ".asm"

##Main function
# create new parser object
newParser = Parser(inputFilename)

# remove comments and extra lines
noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)


# translate vm file into .asm file
# output array here


#add array to new hack file in same path as input
with open(outFile, 'w') as outputFile:
    for line in noCommentsArray:
      outputFile.write(line + "\n")