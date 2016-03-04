import JackTokenizer as jackT
import re


betweenMarkers = r'(?:\> (.*) \<)'

class CompilationEngine:



    def __init__(self, jackTokenizer, outputFile):

        """
        :param jackTokenizer:
        :type jackTokenizer: jackT.JackTokenizer
        :param outputFile:
        :return:
        """

        self.tokenizer = jackTokenizer
        self.outputFile = outputFile
        self.indent = 1
        self.compileClass()

    def compileClass(self):
        # advance twice to get rid of the first tokens tag
        self.tokenizer.advance()
        self.tokenizer.advance()
        self.outputFile.write('<class>\n')
        self.write(self.tokenizer.currentToken) # 'class'
        self.tokenizer.advance()
        self.write(self.tokenizer.currentToken) # 'main'
        self.tokenizer.advance()
        self.write(self.tokenizer.currentToken) # '{'
        self.tokenizer.advance()
        while self.extractedToken() in ('constructor', 'function', 'method'):
            self.compileSubroutine()
        self.outputFile.write('</class>')

    def compileSubroutine(self):
        self.write('<subroutineDec>')
        self.incrIndent()
        self.write(self.tokenizer.currentToken) # should write function/constructor/method
        self.advanceAndWrite() # should write void/type
        self.advanceAndWrite() # should write identifier
        self.advanceAndWrite() # should write (
        self.compileParameterList()
        self.write(self.tokenizer.currentToken) # should write )

        self.compileSubroutineBody()


        # need to close out ) and whatever else comes in end
        self.decrIndent()
        self.write('</subroutineDec>')
        print("compileSubroutine end")

    def compileParameterList(self):
        self.write('<parameterList>')
        self.incrIndent()
        self.tokenizer.advance()
        #parameters
        while self.extractedToken() != ")":
            self.write(self.extractedToken())
            self.tokenizer.advance()

        self.decrIndent()
        self.write('</parameterList>')

    def compileSubroutineBody(self):
        self.write('<subroutineBody>')
        self.incrIndent()
        self.advanceAndWrite() # should be {
        self.tokenizer.advance()

        # print(self.extractedToken())
        while self.extractedToken() != "}":


            while self.extractedToken() == "var":
                self.compileVarDec()  # varDec* statements

            while self.extractedToken() in ('let', 'do'): #('let', 'while', 'if', 'do'):
                self.compileStatements() # compile statements

            self.tokenizer.advance()

        #ultimately }

        self.decrIndent()
        self.write('</subroutineBody>')

    def compileStatements(self):
        self.write('<statements>')
        self.incrIndent()

        if self.extractedToken() == 'let':
            self.compileLet()

        if self.extractedToken() == 'do':
            self.compileDo()

        self.decrIndent()
        self.write('</statements>')

    def compileDo(self):
        self.write('<doStatement>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes "do"
        self.tokenizer.advance()

        while self.extractedToken() != ";":
            self.write(self.tokenizer.currentToken) # writes "do"
            self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes ";"
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</doStatement>')

        print("do called")

    def compileLet(self):
        self.write('<letStatement>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes "let"
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes varName
        self.tokenizer.advance()

        if self.extractedToken() == "[":
            self.write(self.tokenizer.currentToken) # writes [
            self.tokenizer.advance()

            # call expression, for right now very simple
            self.compileExpression()

            self.write(self.tokenizer.currentToken) # writes ]
            self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes =
        self.tokenizer.advance()

        # while self.extractedToken() != ";":
        #     # call expression, for right now very simple
        self.compileExpression()

        self.write(self.tokenizer.currentToken) # writes ;
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</letStatement>')

    def compileExpression(self):
        self.write('<expression>')
        self.incrIndent()


        self.compileTerm() # currently writes term
        # self.tokenizer.advance()

        self.decrIndent()
        self.write('</expression>')

    def compileTerm(self):
        self.write('<term>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes term
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</term>')

    def compileVarDec(self):
        self.write('<varDec>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # should write var
        self.advanceAndWrite() # should write type
        self.advanceAndWrite() # should write varName
        self.tokenizer.advance()

        #if multiple var declarations
        while self.extractedToken() == ',':
            self.write(self.tokenizer.currentToken) #should be ","
            self.tokenizer.advance()
            self.write(self.tokenizer.currentToken) #should be a varName
            self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) #should be a ";"

        self.decrIndent()
        self.write('</varDec>')

    def extractedToken(self):
        token = self.tokenizer.currentToken
        extractedToken = re.findall(betweenMarkers, token)[0]
        return extractedToken

    def advanceAndWrite(self):
        self.tokenizer.advance()
        self.write(self.tokenizer.currentToken)

    def write(self,string):
        self.outputFile.write('  ' * self.indent + string + '\n')

    # increments the tabbing
    def incrIndent(self):
        self.indent += 1

    # decrements the tabbing
    def decrIndent(self):
        self.indent -= 1