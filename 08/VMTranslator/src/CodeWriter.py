# contains methods that actually write the code as well
# as an array that keeps track of the number of time certain code
# segments are used

class CodeWriter:

    # dictionary stores the # of times any label having arguments are used
    labelCounter = 0

    # command types
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    # C_IF = 5
    # C_FUNCTION = 6
    # C_RETURN = 7
    # C_CALL = 8


    # function basename for static variable
    fileBasename = None

    # dictionary with translation of segment names
    segmentDictionary = {
        "local" : "LCL",
        "argument" : "ARG",
        "this" : "THIS",
        "that" : "THAT",
        "temp" : 5,
        "pointer" : 3
    }

    # in case i want to rewrite this to have CodeWriter write directly to file
    # def __init__(self, outputFilePath):
    #
    #     # transforms file into a list of lines
    #     outputFile = open(outputFilePath, 'w')

    def takesFunctionName(self, fileBasename):
        self.fileBasename = fileBasename

    # writes assembly code for all the arithmetic operations
    def writeArithmetic(self, line, outputArray):
        if line.startswith("add"):
            outputArray.append("@SP")
            outputArray.append("AM=M-1")
            outputArray.append("D=M")
            outputArray.append("A=A-1")
            outputArray.append("M=M+D")
        elif line.startswith("sub"):
            outputArray.append("@SP")
            outputArray.append("AM=M-1")
            outputArray.append("D=M")
            outputArray.append("A=A-1")
            outputArray.append("M=M-D")
        elif line.startswith("neg"): # whatever is in y, make it -y
            outputArray.append("D=0")
            outputArray.append("@SP") # call stack pointer
            outputArray.append("A=M-1") # derefrence SP; point to y
            outputArray.append("M=D-M") # negate y by subtracting
        elif line.startswith("eq"):
            outputArray.append("@SP")
            outputArray.append("AM=M-1") #decrement SP and dereference
            outputArray.append("D=M") # D holds y
            outputArray.append("A=A-1") # A points to x
            outputArray.append("D=M-D") # D holds x-y; if =0 then true, else false
            outputArray.append("@FALSE" + str(self.labelCounter))
            outputArray.append("D;JNE")
            outputArray.append("@SP") # true, put -1 on the stack; SP points to TOS after operation
            outputArray.append("A=M-1") # A points to where x was; put -1 there
            outputArray.append("M=-1")
            outputArray.append("@CONTINUE" + str(self.labelCounter))
            outputArray.append("0;JMP")
            outputArray.append("(FALSE" + str(self.labelCounter) + ")")
            outputArray.append("@SP") # false, put 0 on stack; SP points to TOS after operation
            outputArray.append("A=M-1") # A points to where x was; put 0 there
            outputArray.append("M=0")
            outputArray.append("(CONTINUE" + str(self.labelCounter) + ")")
            self.labelCounter += 1 #increment the number
        elif line.startswith("gt"): # if x > y true, else false
            outputArray.append("@SP")
            outputArray.append("AM=M-1") #decrement SP and dereference
            outputArray.append("D=M") # D holds y
            outputArray.append("A=A-1") # A points to x
            outputArray.append("D=M-D") # D holds x-y; if =0 then true, else false
            outputArray.append("@FALSE" + str(self.labelCounter))
            outputArray.append("D;JLE")
            outputArray.append("@SP") # true, put -1 on the stack; SP points to TOS after operation
            outputArray.append("A=M-1") # A points to where x was; put -1 there
            outputArray.append("M=-1")
            outputArray.append("@CONTINUE" + str(self.labelCounter))
            outputArray.append("0;JMP")
            outputArray.append("(FALSE" + str(self.labelCounter) + ")")
            outputArray.append("@SP") # false, put 0 on stack; SP points to TOS after operation
            outputArray.append("A=M-1") # A points to where x was; put 0 there
            outputArray.append("M=0")
            outputArray.append("(CONTINUE" + str(self.labelCounter) + ")")
            self.labelCounter += 1 #increment the number
        elif line.startswith("lt"): # if x < y true, else false
            outputArray.append("@SP")
            outputArray.append("AM=M-1") #decrement SP and dereference
            outputArray.append("D=M") # D holds y
            outputArray.append("A=A-1") # A points to x
            outputArray.append("D=M-D") # D holds x-y; if <0 then true, else false
            outputArray.append("@FALSE" + str(self.labelCounter))
            outputArray.append("D;JGE")
            outputArray.append("@SP") # true, put -1 on the stack; SP points to TOS after operation
            outputArray.append("A=M-1") # A points to where x was; put -1 there
            outputArray.append("M=-1")
            outputArray.append("@CONTINUE" + str(self.labelCounter))
            outputArray.append("0;JMP")
            outputArray.append("(FALSE" + str(self.labelCounter) + ")")
            outputArray.append("@SP") # false, put 0 on stack; SP points to TOS after operation
            outputArray.append("A=M-1") # A points to where x was; put 0 there
            outputArray.append("M=0")
            outputArray.append("(CONTINUE" + str(self.labelCounter) + ")")
            self.labelCounter += 1 #increment the number
        elif line.startswith("and"):
            outputArray.append("@SP") #initialize SP
            outputArray.append("AM=M-1") # dereference and decrement SP
            outputArray.append("D=M") # store y value
            outputArray.append("A=A-1") # point at x
            outputArray.append("M=D&M") # store result of y&x at x
        elif line.startswith("or"):
            outputArray.append("@SP") #initialize SP
            outputArray.append("AM=M-1") # dereference and decrement SP
            outputArray.append("D=M") # store y value
            outputArray.append("A=A-1") # point at x
            outputArray.append("M=D|M") # store result of y or x at x
        elif line.startswith("not"): # pop x push !x
            outputArray.append("@SP") #point at SP
            outputArray.append("A=M-1") # dereference SP
            outputArray.append("M=!M") # invert the value
        else:
            outputArray.append("@2222") # this is my error code

    # write push/
    def writePushPop(self, command, segment, index, outputArray):
        if segment == "constant":
            outputArray.append("@" + index) # initialize value
            outputArray.append("D=A") # store value in register
            outputArray.append("@SP") # initialize SP
            outputArray.append("A=M") # dereference SP
            outputArray.append("M=D") # store value in stack
            outputArray.append("@SP") # advance SP
            outputArray.append("M=M+1")
        elif command == self.C_POP:
            if segment == "local" or segment == "argument" or segment == "this" or segment == "that":
                outputArray.append("@" + self.segmentDictionary[segment]) # point at segment base
                outputArray.append("D=M") # get base address of segment
                outputArray.append("@" + str(index)) #initialize given number
                outputArray.append("D=D+A") # D holds address of RAM location segment[x]
                outputArray.append("@R13") # get temporary address
                outputArray.append("M=D") # put address of segment[x] into a temporary memory location
                outputArray.append("@SP")
                outputArray.append("AM=M-1") # decrement SP and dereference
                outputArray.append("D=M") # D holds the value of the top item on the stack
                outputArray.append("@R13")
                outputArray.append("A=M") # A holds the address of RAM location argument 2 (dereference ptr)
                outputArray.append("M=D") # RAM location argument 2 holds what was on the top of the stack
            elif segment == "temp" or segment == "pointer":
                outputArray.append("@SP")
                outputArray.append("AM=M-1") # decrement SP and dereference
                outputArray.append("D=M") # D holds the value of the top item on the stack
                outputArray.append("@" + str(self.segmentDictionary[segment] + int(index))) #initialize address of temp + index
                outputArray.append("M=D") # place value in correct segment
            elif segment == "static":
                outputArray.append("@SP")
                outputArray.append("AM=M-1") # decrement SP and dereference
                outputArray.append("D=M") # D holds the value of the top item on the stack
                outputArray.append("@" + self.fileBasename + "." + str(index))
                outputArray.append("M=D")
            else:
                outputArray.append("@4444")
        #put contents of RAM location segment[x]onto the stack
        elif command == self.C_PUSH:
            if segment == "local" or segment == "argument" or segment == "this" or segment == "that":
                outputArray.append("@" + self.segmentDictionary[segment])
                outputArray.append("D=M")
                outputArray.append("@" + str(index))
                outputArray.append("A=D+A") # A holds address of segment[x]
                outputArray.append("D=M") # D holds contents of local 3
                outputArray.append("@SP")
                outputArray.append("A=M") # dereference SP
                outputArray.append("M=D") # put D (contents of local 3) on stack
                outputArray.append("@SP")
                outputArray.append("M=M+1") # increment SP
            elif segment == "temp" or segment == "pointer":
                outputArray.append("@" + str(self.segmentDictionary[segment] + int(index))) #initialize address of temp + index
                outputArray.append("D=M") # D holds contents of segment[index]
                outputArray.append("@SP")
                outputArray.append("A=M") # dereference SP
                outputArray.append("M=D") # put D (contents of local 3) on stack
                outputArray.append("@SP")
                outputArray.append("M=M+1") # increment SP
            elif segment == "static":
                outputArray.append("@" + self.fileBasename + "." + str(index)) # constructed correct symbol name
                outputArray.append("D=M") # store saved value in register
                outputArray.append("@SP")
                outputArray.append("A=M") # dereference SP
                outputArray.append("M=D") # put D (contents of local 3) on stack
                outputArray.append("@SP")
                outputArray.append("M=M+1") # increment SP
            else:
                outputArray.append("@6666")
        else:
            outputArray.append("@7777")

    # writes the label takes in the outputArray
    def writeLabel(self, labelName, outputArray):
        # outputArray.append("@" + labelName) #write the label name
        outputArray.append("(" + labelName + ")") #write the label name

    # writes the asm code block for goto label to outputArray
    def writeGotoLabel(self, labelName, outputArray):
        outputArray.append("@" + labelName)
        outputArray.append("D;JMP")

    # writes the asm block for if goto
    def writeIfGoto(self, labelName, outputArray):
        outputArray.append("@SP")
        outputArray.append("AM=M-1") # dereference and decrement stack
        outputArray.append("D=M") # get value at stack (this should be either a 0 for
        outputArray.append("@" + labelName) # queues up correct address
        outputArray.append("D;JNE") # checks if D != 0, this means it's -1 (true)

    # writes the function
    def writeFunction(self, functionName, numLocalVars, outputArray):
        outputArray.append("(" + functionName + ")")
        for num in range(numLocalVars):
            self.writePushPop(self.C_PUSH, "constant", "0", outputArray) # uses previously written write constant

    # # writes the call
    def writeCall(self, functionName, numArgs, outputArray):
        pass

    # writes the return function
    # this is going to get the return address, reset the frame back to the caller
    # and jump back to the caller
    def writeReturn(self, outputArray):
        outputArray.append("// RETURN BEGINS")
        outputArray.append("@LCL") #FRAME = LCL
        outputArray.append("D=M")
        outputArray.append("@FRAME")
        outputArray.append("M=D")
        outputArray.append("@FRAME") # RET = *(FRAME-5)
        outputArray.append("D=M")
        outputArray.append("@5")
        outputArray.append("A=D-A")
        outputArray.append("D=M")
        outputArray.append("@RET")
        outputArray.append("M=D")
        outputArray.append("@SP") # *ARG = pop()
        outputArray.append("AM=M-1")
        outputArray.append("D=M")
        outputArray.append("@ARG")
        outputArray.append("A=M")
        outputArray.append("M=D")
        outputArray.append("@ARG") # SP = ARG + 1
        outputArray.append("D=M+1")
        outputArray.append("@SP")
        outputArray.append("M=D")
        outputArray.append("@FRAME") # THAT = *(FRAME-1)
        outputArray.append("A=M-1")
        outputArray.append("D=M")
        outputArray.append("@THAT")
        outputArray.append("M=D")
        outputArray.append("@FRAME") # THIS = *(FRAME-2)
        outputArray.append("D=M")
        outputArray.append("@2")
        outputArray.append("A=D-A")
        outputArray.append("D=M")
        outputArray.append("@THIS")
        outputArray.append("M=D")
        outputArray.append("@FRAME") # ARG = *(FRAME - 3)
        outputArray.append("D=M")
        outputArray.append("@3")
        outputArray.append("A=D-A")
        outputArray.append("D=M")
        outputArray.append("@ARG")
        outputArray.append("M=D")
        outputArray.append("@FRAME") # LCL = * (FRAME - 4)
        outputArray.append("D=M")
        outputArray.append("@4")
        outputArray.append("A=D-A")
        outputArray.append("D=M")
        outputArray.append("@LCL")
        outputArray.append("M=D")
        outputArray.append("@RET") # goto RET
        outputArray.append("A=M")
        outputArray.append("0;JMP")