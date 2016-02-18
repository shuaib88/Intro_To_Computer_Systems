import sys
import os
from RemoveWhitespace import RemoveWhitespace
from CodeWriter import CodeWriter

import re

class Parser:

    # file read write related
    inputFile = None
    outputArray = []

    # code writer
    codeWriter = None

    # command types
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    C_IF = 5 # using for if-goto commands
    # C_FUNCTION = 6
    # C_RETURN = 7
    # C_CALL = 8

    # Initializer prepares a fresh array
    def __init__(self, inputFile, codeWriter):

        # transforms file into a list of lines
        with open(inputFile, 'r') as initializedFile:
            self.linesArray = initializedFile.readlines()

        #attempting to pass a file name to a coder object
        baseName = os.path.splitext(os.path.basename(os.path.normpath(inputFile)))[0]

        #populate codeWriter with codeWriter object
        self.codeWriter = codeWriter

        #attempting to pass baseName to the coder object
        self.codeWriter.takesFunctionName(baseName)

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
        if len(parsedLine) == 1:
            return self.C_ARITHMETIC
        elif line.startswith("push"):
            return self.C_PUSH
        elif line.startswith("pop"):
            return self.C_POP
        elif line.startswith("label"):
            return self.C_LABEL
        elif line.startswith("goto"):
            return self.C_GOTO
        elif line.startswith("if-goto"):
            return self.C_IF
        else:
            print("commandType did not detect")

    # translates the given line using the definitions and structures
    # stored in CodeWriter
    def translateVMtoASM(self, commentStrippedArray):
        for line in commentStrippedArray:
            if self.commandType(line) == self.C_ARITHMETIC:
                self.codeWriter.writeArithmetic(line, self.outputArray)
            elif self.commandType(line) == self.C_PUSH or self.commandType(line) == self.C_POP:
                parsedLine = line.split()
                command = self.commandType(line)
                segment = parsedLine[1]
                index = parsedLine[2]
                self.codeWriter.writePushPop(command, segment, index, self.outputArray)
            elif self.commandType(line) == self.C_LABEL:
                parsedLine = line.split()
                labelName = parsedLine[1] # this is the label part
                self.codeWriter.writeLabel(labelName, self.outputArray) # write the label to output array label
            elif self.commandType(line) == self.C_GOTO:
                parsedLine = line.split()
                labelName = parsedLine[1] # this is the label part
                self. codeWriter.writeGotoLabel(labelName, self.outputArray) # write the correct code block to output array label
            elif self.commandType(line) == self.C_IF:
                parsedLine = line.split()
                labelName = parsedLine[1] # this is the label part
                self.codeWriter.writeIfGoto(labelName, self.outputArray) # write the label to output array label
            else:
                self.outputArray.append("ERROR")
        return self.outputArray