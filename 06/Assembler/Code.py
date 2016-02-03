# Translates the hack mneumonics for destination, computation, and jumping into binary bits


class Code:

    #dictionary that stores 7 bit code of computation mnemonic
    compDictionary = {
        '0'  : '0101010',
        '1'  : '0111111',
        '-1' : '0111010',
        'D'  : '0001100',
        'A'  : '0110000',
        '!D' : '0001101',
        '!A' : '0110001',
        '-D' : '0011111',
        '-A' : '0110011',
        'D+1': '0111111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        'M'  : '1110000',
        '!M' : '1110001',
        '-M' : '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'D+M': '1000010',
        'D-M': '1010011',
        'M-D': '1000111',
        'D&M': '1000000',
        'D|M': '1010101'
    }

    # dictionary with the codes for the destination
    destDictionary = {
        'null'   : '000', # not sure if this should be empty string or space
        'M'  : '001',
        'D'  : '010',
        'MD' : '011',
        'A'  : '100',
        'AM' : '101',
        'AD' : '110',
        'AMD': '111'
    }

    # dictionary with the codes for the jump
    jumpDictionary = {
        'null'   : '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }





    #parameter: inputString - desired computation, output: code for the computation
    def comp(self, inputString):
        return self.compDictionary[inputString]

    #parameter: inputString - the destination mnemonic eg: D, M, DM, etc..
    def dest(self, inputString):
        return self.destDictionary[inputString]

    #parameter: inputString - the destination mnemonic for jumps. output: code for the jump
    def jump(self, inputString):
        return self.jumpDictionary[inputString]