#this file drives the whole assembler and uses the other included packages

import sys

import os

from Parser import Parser

from RemoveWhiteSpace import RemoveWhitespace



#extract filename and root from filename
script, inputFilename = sys.argv
rootName = os.path.splitext(inputFilename)[0]
print(rootName)

#declare output file path
outFile = rootName + ".hack"

##Main function
# create new parser object
newParser = Parser(inputFilename)

# remove whitespace
noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)

#remove label, populate symbol table
labelStrippedArray = newParser.stripLabels(noCommentsArray)

#replace @symbols with proper numerical addresses
cleanArray = newParser.replaceAtDeclarations(labelStrippedArray)

#translate clean code to machine code
atValueArray = newParser.translateToMachineCode(cleanArray)

#add array to new hack file in same path as input
with open(outFile, 'w') as outputFile:
    for line in atValueArray:
      outputFile.write(line + "\n")