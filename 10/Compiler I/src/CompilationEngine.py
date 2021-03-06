import JackTokenizer as jackT
import re


betweenMarkers = r'(?:\> (.*) \<)'
operation = ['+','-','*','/','&amp;','|','&lt;','&gt;','=']
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
        self.outputFile.write('<class>\n')
        self.writeAndAdvance() # 'class'
        self.writeAndAdvance() # 'main'
        self.writeAndAdvance() # '{'

        while self.extractedToken() in ('static', 'field'):
            self.compileClassVarDec()

        while self.extractedToken() in ('constructor', 'function', 'method'):
            self.compileSubroutine()

        self.write(self.tokenizer.currentToken) # writes ";"
        self.outputFile.write('</class>')

    def compileClassVarDec(self):
        self.write('<classVarDec>')
        self.incrIndent()

        self.writeAndAdvance() # 'static' | 'field'
        self.writeAndAdvance() # type
        self.writeAndAdvance() # identifier

        #if multiple var declarations
        while self.extractedToken() == ',':
            self.writeAndAdvance() #should be ","
            self.writeAndAdvance() #should be a varName

        self.writeAndAdvance() #should be ;

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
            self.writeAndAdvance()
            if self.extractedToken() == ",":
                self.writeAndAdvance()

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

        self.writeAndAdvance()# writes "}"

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

        self.writeAndAdvance() # writes "if"
        self.writeAndAdvance() # writes "("

        self.compileExpression()
        self.writeAndAdvance() # writes ")"

        self.writeAndAdvance() # writes "{"

        # need statements
        self.compileStatements()

        # need close bracket
        self.writeAndAdvance() # writes "}"

        self.decrIndent()
        self.write('</ifStatement>')


    def compileReturn(self):
        self.write('<returnStatement>')
        self.incrIndent()

        self.writeAndAdvance() # writes "return"

        if self.extractedToken() != ";":
            self.compileExpression()    #if return should return an expression

        self.writeAndAdvance() # writes ";"

        self.decrIndent()
        self.write('</returnStatement>')

    def compileWhile(self):
        self.write('<whileStatement>')
        self.incrIndent()

        self.writeAndAdvance() # writes "while"
        self.writeAndAdvance() # writes "("

        self.compileExpression()

        self.writeAndAdvance() # writes ")"
        self.writeAndAdvance() # writes "{"

        # need statements
        self.compileStatements()

        # need close bracket
        self.writeAndAdvance() # writes "}"

        self.decrIndent()
        self.write('</whileStatement>')


    def compileDo(self):
        self.write('<doStatement>')
        self.incrIndent()

        self.writeAndAdvance() # writes "do"

        while self.extractedToken() != ";":


            if self.extractedToken() == "(":
                self.writeAndAdvance() # writes the "("

                #call expression list
                self.compileExpressionList()

            self.writeAndAdvance() # writes the subroutine tokens

        self.writeAndAdvance() # writes ";"

        self.decrIndent()
        self.write('</doStatement>')

    def compileExpressionList(self):
        self.write('<expressionList>')
        self.incrIndent()

        # will fill this out when have more expressions
        while self.extractedToken() != ")":

            self.compileExpression() # should write expression

            if self.extractedToken() == ",": # should write "," if there are more expressions
                self.writeAndAdvance()

        self.decrIndent()
        self.write('</expressionList>')

    def compileLet(self):
        self.write('<letStatement>')
        self.incrIndent()

        self.writeAndAdvance() # writes "let"
        self.writeAndAdvance() # writes varName

        if self.extractedToken() == "[":
            self.writeAndAdvance() # writes [

            self.compileExpression()

            self.writeAndAdvance() # writes ]

        self.writeAndAdvance() # writes =

        # while self.extractedToken() != ";":
        #     # call expression, for right now very simple
        self.compileExpression()

        self.writeAndAdvance() # writes ;

        self.decrIndent()
        self.write('</letStatement>')

    def compileExpression(self):
        self.write('<expression>')
        self.incrIndent()

        self.compileTerm() # writes first term

        while self.extractedToken() in operation:
            self.writeAndAdvance() # writes operation
            self.compileTerm()

        self.decrIndent()
        self.write('</expression>')

    def compileTerm(self):
        self.write('<term>')
        self.incrIndent()

        #checks for appropriate term time

        if self.extractedToken() == "(":
            self.writeAndAdvance() # write "("
            self.compileExpression()
            self.writeAndAdvance() # write ")"

        elif self.extractedToken() in ["-", "~"]:
            self.writeAndAdvance() # write unaryOperator
            self.compileTerm() #write term

        elif self.lookahead() in [".", "("]:
            self.compileSubroutineCall()

        elif self.lookahead() == "[":
            self.writeAndAdvance() # varName
            self.writeAndAdvance() # write "["
            self.compileExpression()
            self.writeAndAdvance() # write "]"

        else:
            #ELSE SIMPLE (MAYBE CHECK) - token type [IntConst, str-const, keyword, Identifier or Unary OP
                ## integerConstant | stringConstant | keywordConstant | varName | | unaryOp term
            self.writeAndAdvance() # should print one of the above

        self.decrIndent()
        self.write('</term>')

    def compileSubroutineCall(self):

        if self.lookahead() == ".": #
            self.writeAndAdvance() # write className | varName
            self.writeAndAdvance() # write "."
            self.writeAndAdvance() # write subroutineName
            self.writeAndAdvance() # write "("
            self.compileExpressionList()
            self.writeAndAdvance() # write ")"

        elif self.lookahead() == "(":
            self.writeAndAdvance() # write subroutineName
            self.writeAndAdvance() # write "("
            self.compileExpressionList()
            self.writeAndAdvance() # write ")"

    def compileVarDec(self):

        self.write('<varDec>')
        self.incrIndent()

        self.writeAndAdvance() # should write var
        self.writeAndAdvance() # should write type
        self.writeAndAdvance() # should write varNma

        #if multiple var declarations
        while self.extractedToken() == ',':
            self.writeAndAdvance() #should be ","
            self.writeAndAdvance() #should be a varName

        self.writeAndAdvance() #should be a ";"

        self.decrIndent()
        self.write('</varDec>')

    def lookahead(self):
        nextToken = self.tokenizer.tokens[0] # full token with tags
        extractedToken = re.findall(betweenMarkers, nextToken)[0]
        return extractedToken

    def extractedToken(self):
        token = self.tokenizer.currentToken
        extractedToken = re.findall(betweenMarkers, token)[0]
        return extractedToken

    def advanceAndWrite(self):
        self.tokenizer.advance()
        self.write(self.tokenizer.currentToken)

    def writeAndAdvance(self):
        self.write(self.tokenizer.currentToken)
        self.tokenizer.advance()

    def write(self,string):
        # self.outputFile.write('  ' * self.indent + string )
        self.outputFile.write('  ' * self.indent + string + '\n')

    # increments the tabbing
    def incrIndent(self):
        self.indent += 1

    # decrements the tabbing
    def decrIndent(self):
        self.indent -= 1