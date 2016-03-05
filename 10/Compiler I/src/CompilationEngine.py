import JackTokenizer as jackT
import re


betweenMarkers = r'(?:\> (.*) \<)'

statements = ['let', 'do', 'while', 'if']

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
        # self.outputFile.write('<class>')
        self.outputFile.write('<class>\n')
        self.write(self.tokenizer.currentToken) # 'class'
        self.tokenizer.advance()
        self.write(self.tokenizer.currentToken) # 'main'
        self.tokenizer.advance()
        self.write(self.tokenizer.currentToken) # '{'
        self.tokenizer.advance()

        while self.extractedToken() in ('static', 'field'):
            self.compileClassVarDec()

        while self.extractedToken() in ('constructor', 'function', 'method'):
            self.compileSubroutine()

        self.write(self.tokenizer.currentToken) # writes ";"
        self.outputFile.write('</class>')

    def compileClassVarDec(self):
        self.write('<classVarDec>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # 'static' | 'field'
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # type
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # identifier
        self.tokenizer.advance()

        #if multiple var declarations
        while self.extractedToken() == ',':
            self.write(self.tokenizer.currentToken) #should be ","
            self.tokenizer.advance()
            self.write(self.tokenizer.currentToken) #should be a varName
            self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) #should be ;
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</classVarDec>')


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


        while self.extractedToken() != "}":

            while self.extractedToken() == "var":
                self.compileVarDec()  # varDec* statements

            while self.extractedToken() in statements:
                self.compileStatements() # compile statements

        self.write(self.tokenizer.currentToken) # writes "}"
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</subroutineBody>')

    def compileStatements(self):
        self.write('<statements>')
        self.incrIndent()


        while self.extractedToken() in statements:

            if self.extractedToken() == 'let':
                self.compileLet()

            elif self.extractedToken() == 'do':
                self.compileDo()

            elif self.extractedToken() == 'while':
                self.compileWhile()

            elif self.extractedToken() == 'if':
                self.compileIf()


        if self.extractedToken() == 'return':
            self.compileReturn()


        self.decrIndent()
        self.write('</statements>')

    def compileIf(self):
        self.write('<ifStatement>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes "if"
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes "("
        self.tokenizer.advance()

        self.compileExpression()

        self.write(self.tokenizer.currentToken) # writes ")"
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes "{"
        self.tokenizer.advance()

        # need statements
        self.compileStatements()

        # need close bracket
        self.write(self.tokenizer.currentToken) # writes "}"
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</ifStatement>')


    def compileReturn(self):
        self.write('<returnStatement>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes "return"
        self.tokenizer.advance()

        if self.extractedToken() != ";":
            self.compileExpression()    #if return should return an expression

        self.write(self.tokenizer.currentToken) # writes ";"
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</returnStatement>')

    def compileWhile(self):
        self.write('<whileStatement>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes "while"
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes "("
        self.tokenizer.advance()

        self.compileExpression()

        self.write(self.tokenizer.currentToken) # writes ")"
        self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes "{"
        self.tokenizer.advance()

        # need statements
        self.compileStatements()

        # need close bracket
        self.write(self.tokenizer.currentToken) # writes "}"
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</whileStatement>')


    def compileDo(self):
        self.write('<doStatement>')
        self.incrIndent()

        self.write(self.tokenizer.currentToken) # writes "do"
        self.tokenizer.advance()

        while self.extractedToken() != ";":


            if self.extractedToken() == "(":
                self.write(self.tokenizer.currentToken) # writes the "("
                self.tokenizer.advance()

                #call expression list
                self.compileExpressionList()

            self.write(self.tokenizer.currentToken) # writes the subroutine tokens
            self.tokenizer.advance()

        self.write(self.tokenizer.currentToken) # writes ";"
        self.tokenizer.advance()

        self.decrIndent()
        self.write('</doStatement>')

    def compileExpressionList(self):
        self.write('<expressionList>')
        self.incrIndent()

        # will fill this out when have more expressions
        while self.extractedToken() != ")":
            self.compileExpression()

        self.decrIndent()
        self.write('</expressionList>')

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
        self.tokenizer.advance()

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
        # self.outputFile.write('  ' * self.indent + string )
        self.outputFile.write('  ' * self.indent + string + '\n')

    # increments the tabbing
    def incrIndent(self):
        self.indent += 1

    # decrements the tabbing
    def decrIndent(self):
        self.indent -= 1