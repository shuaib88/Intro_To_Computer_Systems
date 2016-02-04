# Parser: Encapsulates access to the input code. Reads an assembly language
# com- mand, parses it, and provides convenient access to the
# command’s components (fields and symbols). In addition, removes
# all white space and comments.

from removeWhiteSpace import removeWhitespace
import re
from Code import Code

class Parser:

    # files
    inputFile = None
    outputArray = []
    outputFile = None

    # command types
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

    # regexes
    code = Code()

    # Initializer prepares a fresh array
    def __init__(self, inputFile):

        # transforms file into a list of lines
        with open(inputFile, 'r') as initializedFile:
            self.linesArray = initializedFile.readlines()

        #initializes counters which we'll need later
        self.command = ''
        self.currentLineNumber = 0

    # checks if there are more commands to process
    def hasMoreCommands(self):
        if self.currentLineNumber - 1 < len(self.linesArray):
            return True
        else:
            return False

    # Reads the next command from the input and makes it the current
    # command. Should be called only if hasMoreCommands() is true.
    # Initially there is no current command.
    def advance(self):
        # grab a line
        if self.hasMoreCommands():
            command = self.linesArray[self.currentLineNumber]
            self.currentLineNumber += 1

        # make the valid command line a line

    # checks the type of the command
    def commandType(self, line):
        if line.startswith("@"):
            return self.A_COMMAND

        else:
            return self.C_COMMAND

    # takes a clean array (no labels) and starts translating directly to machine code
    def translateToMachineCode(self, cleanArray):
        for line in cleanArray:
            if self.commandType(line) == self.A_COMMAND:
                decimalValue = line.partition("@")[2]

                self.outputArray.append(decimalValue)
            elif self.commandType(line) == self.C_COMMAND:
                pass
            elif self.commandType(line) == self.L_COMMAND:
                pass
        return self.outputArray


# IF it's an @ statement
    # take the numbers after and store to a new array
# ELIF it's a command statement
    #


##Main function
# create new parser object
newParser = Parser("testFile.in")

# remove whitespace
noCommentsArray = removeWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)

atValueArray = newParser.translateToMachineCode(noCommentsArray)

print(atValueArray)


