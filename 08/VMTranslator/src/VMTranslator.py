import sys

import os

from Parser import Parser

from RemoveWhitespace import RemoveWhitespace

from CodeWriter import CodeWriter

## main function to be moved to VMTranslator

#extract filename and root from filename
# script, inputFilename = sys.argv
inputFilename = "/Users/shuaibahmed/Code/Intro_Computer_Sys/nand2tetris/projects/08/ProgramFlow/FibonacciSeries/FibonacciSeries.vm"
rootName = os.path.splitext(inputFilename)[0]
# get basename for CodeWriter's use

#declare output file path
outFile = rootName + ".asm"

# declare codewriter to pass to parser
newCodeWriter = CodeWriter()

##Main function
# create new parser object
newParser = Parser(inputFilename, newCodeWriter)

# remove comments and extra lines
noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)

# translate vm file into .asm file
# output array here
outputArray = newParser.translateVMtoASM(noCommentsArray)

#add array to new hack file in same path as input
with open(outFile, 'w') as outputFile:
    for line in outputArray:
      outputFile.write(line + "\n")