import sys

import os

from os.path import normpath, basename

from Parser import Parser

from RemoveWhitespace import RemoveWhitespace

from CodeWriter import CodeWriter

## Main function of the VMTranslator
# handles single file or directory
script, attemptedPathInput = sys.argv

# file or directory handling:
if os.path.isdir(attemptedPathInput):
    directoryPath = attemptedPathInput

else:
    directoryPath = os.path.dirname(os.path.abspath(attemptedPathInput))
    print("attempt single file's directoryPath")
    print(directoryPath)

# create code writer
newCodeWriter = CodeWriter()

#determine output file path
directoryBase = basename(normpath(directoryPath))
outFile = directoryPath + "/" + directoryBase + ".asm"

# declare array to store all our values
masterOutputArray = []

for inputFile in os.listdir(directoryPath):

    if inputFile.endswith(".vm"):

        # add path to file name
        fullPathInputFile = directoryPath + "/" + inputFile

        # create new parser object
        newParser = Parser(fullPathInputFile, newCodeWriter)

        # remove comments and extra lines
        noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)

        # for debugging code: adds file name
        outputArray = []
        outputArray.append("//" + inputFile)

        #output array from my Parser
        newParserOutput = newParser.translateVMtoASM(noCommentsArray)

        # translate vm file into .asm file
        # tack on Parser output to debug code
        outputArray.extend(newParserOutput)

        #extend our master output array
        masterOutputArray.extend(outputArray)

#add array to new hack file in same path as input
with open(outFile, 'w') as outputFile:
    for line in masterOutputArray:
        outputFile.write(line + "\n")