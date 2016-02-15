import sys
import os
from RemoveWhitespace import RemoveWhitespace
from CodeWriter import CodeWriter

import re

class Parser:

    # file read write related
    inputFile = None
    outputArray = []

    # code writer object
    newCodeWriter = CodeWriter()

    # command types
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    # C_LABEL = 3
    # C_GOTO = 4
    # C_IF = 5
    # C_FUNCTION = 6
    # C_RETURN = 7
    # C_CALL = 8


    # Initializer prepares a fresh array
    def __init__(self, inputFile):

        # transforms file into a list of lines
        with open(inputFile, 'r') as initializedFile:
            self.linesArray = initializedFile.readlines()

    # checks if there are more commands to process
    def hasMoreCommands(self):
        if self.currentLineNumber - 1 < len(self.linesArray):
            return True
        else:
            return False

    # returns the command type of the line
    # this week it's arithmetic push or pop
    def commandType(self, line):
        parsedLine = line.split()
        # 1 line is arithmetic
        if len(parsedLine) == 1:
            return self.C_ARITHMETIC
        elif line.startswith("push"):
            return self.C_PUSH
        elif line.startswith("pop"):
            return self.C_POP

    # translates the given line using the definitions and structures
    # stored in CodeWriter
    def translateVMtoASM(self, commentStrippedArray):
        for line in commentStrippedArray:
            if self.commandType(line) == self.C_ARITHMETIC:
                self.newCodeWriter.writeArithmetic(line, self.outputArray)
            elif self.commandType(line) == self.C_PUSH:
                parsedLine = line.split()
                command = self.commandType(parsedLine[0])
                segment = parsedLine[1]
                index = parsedLine[2]
                self.newCodeWriter.writePushPop(command, segment, index, self.outputArray)
            elif self.commandType(line) == self.C_POP:
                self.outputArray.append("POP")
            else:
                self.outputArray.append("ERROR")
        return self.outputArray


## main function to be moved to VMTranslator

#extract filename and root from filename
# script, inputFilename = sys.argv
inputFilename = "/Users/shuaibahmed/Code/Intro_Computer_Sys/nand2tetris/projects/07/StackArithmetic/StackTest/StackTest.vm"
rootName = os.path.splitext(inputFilename)[0]

#declare output file path
outFile = rootName + ".asm"


##Main function
# create new parser object
newParser = Parser(inputFilename)

# remove comments and extra lines
noCommentsArray = RemoveWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)


# translate vm file into .asm file
# output array here
outputArray = newParser.translateVMtoASM(noCommentsArray)


#add array to new hack file in same path as input
with open(outFile, 'w') as outputFile:
    for line in outputArray:
      outputFile.write(line + "\n")