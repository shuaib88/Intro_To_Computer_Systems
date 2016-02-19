import sys

import os

from os.path import normpath, basename

import glob

from Parser import Parser

from RemoveWhitespace import RemoveWhitespace

from CodeWriter import CodeWriter

## main function to be moved to VMTranslator

# #extract filename and root from filename
# # script, inputFilename = sys.argv
# inputFilename = "/Users/shuaibahmed/Code/Intro_Computer_Sys/nand2tetris/projects/08/FunctionCalls/FibonacciElement"
# rootName = os.path.splitext(inputFilename)[0]
# # get basename for CodeWriter's use
#
# #declare output file path
# outFile = rootName + ".asm"
#
# # declare codewriter to pass to parser
# newCodeWriter = CodeWriter()
#
# ##Main function
# # create new parser object
# newParser = Parser(inputFilename, newCodeWriter)
#
# # remove comments and extra lines
# noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)
#
# # translate vm file into .asm file
# # output array here
# outputArray = newParser.translateVMtoASM(noCommentsArray)
#
# #add array to new hack file in same path as input
# with open(outFile, 'w') as outputFile:
#     for line in outputArray:
#       outputFile.write(line + "\n")



##
##
## Code for if the input is a directory file

# if input path is file
    # run existing code above

# else:
    # run code below

script, attemptedPathInput = sys.argv

if os.path.isdir(attemptedPathInput):
    directoryPath = attemptedPathInput

else:
    directoryPath = os.path.dirname(os.path.abspath(attemptedPathInput))
    print("attempt single file's directoryPath")
    print(directoryPath)

# directoryPath = "/Users/shuaibahmed/Code/Intro_Computer_Sys/nand2tetris/projects/08/FunctionCalls/StaticsTest"

directoryBase = basename(normpath(directoryPath))

print("directoryBase:")
print(directoryBase)

# create code writer
newCodeWriter = CodeWriter()

#declare output file path
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