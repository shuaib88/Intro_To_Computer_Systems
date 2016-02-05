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

    # command types
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

    # regexes
    code = Code()

    # symbol table
    symbolTable = {}
    symbolMemoryAddress = 16

    # Initializer prepares a fresh array
    def __init__(self, inputFile):

        # transforms file into a list of lines
        with open(inputFile, 'r') as initializedFile:
            self.linesArray = initializedFile.readlines()

        #initializes counters which we'll need later
        self.command = ''
        self.currentLineNumber = 0
        self.code = Code()

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

        elif line.startswith("(") and line.endswith(")"):
            return self.L_COMMAND

        else:
            return self.C_COMMAND

    def stripLabels(self, cleanArray):
        labelStrippedArray = []
        for line in cleanArray:
            #for label declarations
            if self.commandType(line) == 2:
                label = line[1:-1]
                if label in self.symbolTable:
                    pass
                else:
                    self.symbolTable[label] = self.currentLineNumber

            # if neither of two add to
            else:
                labelStrippedArray.append(line)
                self.currentLineNumber += 1
            print(self.currentLineNumber)
        return labelStrippedArray
    # for processing and replacing @symbols with correct addresses
    def replaceAtDeclarations(self, labelStrippedArray):
        pureAssembyArray = []
        for line in labelStrippedArray:
            # if an @symbol command
            if self.commandType(line) == 0 and re.search('[A-Za-z_.$:]', line[1]):
                symbol = line.partition("@")[2]
                # for symbols in the table swap symbolic address with numeric address
                if symbol in self.symbolTable:
                    symbolAddress = self.symbolTable[symbol]
                    symbolAddressString = str(symbolAddress)
                    print("symbolTable Value")
                    print(type(self.symbolTable[symbol]))
                    replacedLine = "@" + symbolAddressString
                    pureAssembyArray.append(replacedLine)
                    self.currentLineNumber += 1
                #for symbols not in the table they must be var addresses, address them
                else:
                    self.symbolTable[symbol] = self.symbolMemoryAddress
                    symbolAddressString = str(self.symbolMemoryAddress)
                    self.symbolMemoryAddress += 1
                    replacedLine = "@" + symbolAddressString
                    pureAssembyArray.append(replacedLine)
            else:
                pureAssembyArray.append(line)
        return pureAssembyArray


    # takes a clean array (no labels) and starts translating directly to machine code
    def translateToMachineCode(self, cleanArray):
        # first three litters of CInstruction
        cInstructionStarterString = "111"

        for line in cleanArray:
            if self.commandType(line) == self.A_COMMAND:
                decimalValueStr = line.partition("@")[2]
                decimalValueInt = int(decimalValueStr)
                binaryValue = "{0:015b}".format(decimalValueInt)
                self.outputArray.append("0" + binaryValue)

            elif self.commandType(line) == self.C_COMMAND:
                # straight C command
                if ("=" not in line) and (";" not in line):
                    cBinaryString = self.code.comp(line)
                    destString = self.code.dest("null")
                    jumpString = self.code.jump("null")
                    self.outputArray.append(cInstructionStarterString + \
                                            cBinaryString + destString + jumpString)
                # dest = comp command
                elif ("=" in line) and (";" not in line):
                    parsedOnEqual = line.partition("=")
                    cBinaryString = self.code.comp(parsedOnEqual[2])
                    destString = self.code.dest(parsedOnEqual[0])
                    jumpString = self.code.jump("null")
                    self.outputArray.append(cInstructionStarterString + \
                                            cBinaryString + destString + jumpString)
                # comp;JMP command
                elif ("=" not in line) and (";" in line):
                    parsedOnSemicolon = line.partition(";")
                    cBinaryString = self.code.comp(parsedOnSemicolon[0])
                    destString = self.code.dest("null")
                    jumpString = self.code.jump(parsedOnSemicolon[2])
                    self.outputArray.append(cInstructionStarterString + \
                                            cBinaryString + destString + jumpString)
                # dest = comp; jump
                elif ("=" in line) and (";" in line):
                    equalsIndex = line.index("=")
                    semicolonIndex = line.index(";")
                    cBinaryString = self.code.comp(line[equalsIndex+1:semicolonIndex])
                    destString = self.code.dest(line[0:equalsIndex])
                    jumpString = self.code.jump(line[semicolonIndex+1:len(line)])
                    self.outputArray.append(cInstructionStarterString + \
                                            cBinaryString + destString + jumpString)

            elif self.commandType(line) == self.L_COMMAND:
                pass
        return self.outputArray


##Main function
# create new parser object
testFile = "test.asm"
newParser = Parser(testFile)

# remove whitespace
noCommentsArray = removeWhitespace.removeWhiteSpaceAndComments(newParser.linesArray)

# print("white spaced removed:")
# print(noCommentsArray)

#remove label, populate symbol table
labelStrippedArray = newParser.stripLabels(noCommentsArray)

print("label stripped")
print(labelStrippedArray)

print("symbol table after label stripped")
print(newParser.symbolTable)

#replace @symbols with proper numerical addresses
cleanArray = newParser.replaceAtDeclarations(labelStrippedArray)

print("clean array")
print(cleanArray)

print("symbol table after @declarations replaced")
print(newParser.symbolTable)


#translate clean code to machine code
atValueArray = newParser.translateToMachineCode(cleanArray)

print("cleaned code:")
print(atValueArray)



# debug length of commands
# for line in atValueArray:
#     print(len(line))


#add array to new hackfile
fileName = testFile.partition(".")
outFile = fileName[0] + ".hack"
with open(outFile, 'w') as outputFile:
    for line in atValueArray:
      outputFile.write(line + "\n")

