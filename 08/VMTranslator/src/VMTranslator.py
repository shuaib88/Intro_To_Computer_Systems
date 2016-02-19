import sys

import os

from os.path import normpath, basename

import glob

from Parser import Parser

from RemoveWhitespace import RemoveWhitespace

from CodeWriter import CodeWriter

## main function to be moved to VMTranslator

#extract filename and root from filename
# script, inputFilename = sys.argv
inputFilename = "/Users/shuaibahmed/Code/Intro_Computer_Sys/nand2tetris/projects/08/FunctionCalls/SimpleFunction/SimpleFunction.vm"
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



# ##
# ##
# ## Code for if the input is a directory file
#
# # if input path is file
#     # run existing code above
#
# # else:
#     # run code below
#
# directoryPath = "/Users/shuaibahmed/Code/Intro_Computer_Sys/nand2tetris/projects/08/TestDirectory"
#
# directoryBase = basename(normpath(directoryPath))
#
# # create code writer
# newCodeWriter = CodeWriter()
#
# #declare output file path
# # outFile = directoryPath + "/outFile.asm"
# outFile = directoryPath + "/" + directoryBase + ".asm"
#
# # declare array to store all our values
# masterOutputArray = []
#
# for inputFile in os.listdir(directoryPath):
#
#     if inputFile.endswith(".vm"):
#
#         # add path to file name
#         fullPathInputFile = directoryPath + "/" + inputFile
#
#         # create new parser object
#         newParser = Parser(fullPathInputFile, newCodeWriter)
#
#         # remove comments and extra lines
#         noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)
#
#         # translate vm file into .asm file
#         # output array here
#         outputArray = newParser.translateVMtoASM(noCommentsArray)
#
#         #extend our master output array
#         # masterOutputArray.extend(outputArray)
#
# #add array to new hack file in same path as input
# with open(outFile, 'w') as outputFile:
#     for line in outputArray:
#         outputFile.write(line + "\n")