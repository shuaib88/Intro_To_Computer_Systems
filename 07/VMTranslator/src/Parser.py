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
    # newCodeWriter = CodeWriter()

    # code writer
    codeWriter = None

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
    def __init__(self, inputFile, codeWriter):

        # transforms file into a list of lines
        with open(inputFile, 'r') as initializedFile:
            self.linesArray = initializedFile.readlines()

        #attempting to pass a file name to a coder object
        baseName = os.path.splitext(os.path.basename(os.path.normpath(inputFile)))[0]

        #populate codeWriter with codeWriter object
        self.codeWriter = codeWriter

        # #attempting to pass baseName to the coder object
        # self.newCodeWriter.takesFunctionName(baseName)

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
                # self.newCodeWriter.writeArithmetic(line, self.outputArray)
                self.codeWriter.writeArithmetic(line, self.outputArray)
            elif self.commandType(line) == self.C_PUSH or self.C_POP:
                parsedLine = line.split()
                command = self.commandType(line)
                segment = parsedLine[1]
                index = parsedLine[2]
                # self.newCodeWriter.writePushPop(command, segment, index, self.outputArray)
                self.codeWriter.writePushPop(command, segment, index, self.outputArray)
            else:
                self.outputArray.append("ERROR")
        return self.outputArray