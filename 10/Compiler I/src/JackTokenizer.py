# JackTokenizer: Removes all comments and white space from the input stream
# and breaks it into Jack- language tokens, as specified by the Jack grammar

# needs an array that is going to hold a token at a time

import re

#attribution - hint for pattern recognizer from https://github.com/josephchandlerjr/Nand2Tetris/blob/master/CompilerI/JackTokenizer.py
#attribution - http://regexr.com to test
string = r'(?:"[^"]*")' #my version
comment = r'(?:\/\/[^\n]*\n)|(?:\/\*\*(?:.|\n)*?\*\/)' # my version
delimiters = r'[\(\)\[\]\{\}\,\;\=\.\+\-\*\/\&\|\~\<\>]|'+string+'| *' #attributed
keywords = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else','while','return']
symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|','<', '>', '=', '~']

class JackTokenizer:

    def __init__(self, inputFile):
        self.inputString = open(inputFile, 'r').read() # turns whole file into one string
        self.cleanInputFile() # removes comments and transforms all white space to single space
        self.tokensUnmarked = [token for token in re.split(r'('+ delimiters + r')',self.inputString) if token not in ('', ' ', None)]
        self.tokens = []
        self.markTokens()
        self.currentToken = None

    def cleanInputFile(self):
        self.inputString = " ".join(re.sub(comment,"",self.inputString).split())

    def hasMoreTokens(self):
        if not self.tokens:
            return False
        else:
            return True

    def markTokens(self):
        self.tokens.append("<tokens>")
        for unmarkedToken in self.tokensUnmarked:
            if self.tokenType(unmarkedToken) == 'KEYWORD':
                self.tokens.append("<keyword> " + unmarkedToken + " </keyword>")
            elif self.tokenType(unmarkedToken) == 'SYMBOL': # noted special symbol swaps
                if unmarkedToken == "<":
                    unmarkedToken = "&lt;"
                if unmarkedToken == ">":
                    unmarkedToken = "&gt;"
                if unmarkedToken == "&":
                    unmarkedToken = "&amp;"
                if unmarkedToken == "\"":
                    unmarkedToken = "&quot;"
                self.tokens.append("<symbol> " + unmarkedToken + " </symbol>")
            elif self.tokenType(unmarkedToken) == 'IDENTIFIER':
                self.tokens.append("<identifier> " + unmarkedToken + " </identifier>")
            elif self.tokenType(unmarkedToken) == 'STRING_CONST':
                self.tokens.append("<stringConstant> " + unmarkedToken.strip("\"") + " </stringConstant>")
            elif self.tokenType(unmarkedToken) == 'INT_CONST':
                self.tokens.append("<integerConstant> " + unmarkedToken.strip("\"") + " </integerConstant>")
            else:
                self.tokens.append("DID NOT DETECT TOKEN: " + unmarkedToken)
                print("error marking tokens")
        self.tokens.append("</tokens>")

    def tokenType(self, unmarkedToken):
        if unmarkedToken in keywords:
            return 'KEYWORD'
        if unmarkedToken in symbols:
            return 'SYMBOL'
        if unmarkedToken.startswith("\""):
            return 'STRING_CONST'
        if unmarkedToken.isdigit():
            return 'INT_CONST'
        else:
            return 'IDENTIFIER'

    def advance(self):
        self.currentToken = self.tokens.pop(0) # pops off first token in array




