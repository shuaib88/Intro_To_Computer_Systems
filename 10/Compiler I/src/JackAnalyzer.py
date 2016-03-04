import JackTokenizer as jackModule
import CompilationEngine as compE
import sys
import os

# 1. Create a JackTokenizer from the Xxx.jack input file;
# 2. Create an output file called Xxx.xml and prepare it for writing;
# 3. Use the CompilationEngine to compile the input JackTokenizer into the output file.

## step 1 just tokenize

# read input directory or file folder
attemptedPath = sys.argv[1]

if os.path.isdir(attemptedPath):
    directoryPath = attemptedPath

else:
    directoryPath = os.path.dirname(attemptedPath)

# create the output file
for fileName in os.listdir(directoryPath):
    if fileName.endswith(".jack"):

        # add path to file name
        fullPathInputFile = directoryPath + "/" + fileName

        # instantiate a new jack tokenizer
        tokenizer = jackModule.JackTokenizer(fullPathInputFile)

        #output file
        outputFileName = directoryPath + "/" + os.path.splitext(fileName)[0] + "Shuaib.xml"
        with open(outputFileName, 'w') as outputFile:

            compilationEngine = compE.CompilationEngine(tokenizer, outputFile)

            pass
            # prints all the tokens
            # for token in tokenizer.tokens:
            #     # outputFile.write(token + "\n") # attempt to write tokenized file
            #     # outputFile.write("->" + tokenizer.tokenType(token) + "\n")
            #     outputFile.write(token + "\n") # attempt to write tokenized file

            # while tokenizer has tokens

                # write currentToken to file




