# contains methods that actually write the code as well
# as an array that keeps track of the number of time certain code
# segments are used

class CodeWriter:

    # dictionary stores the # of times any label having arguments are used
    labelCounter = 0

    # in case i want to rewrite this to have CodeWriter write directly to file
    # def __init__(self, outputFilePath):
    #
    #     # transforms file into a list of lines
    #     outputFile = open(outputFilePath, 'w')

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
            outputArray.append("@1111")


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
        else:
            outputArray.append("ERROR")