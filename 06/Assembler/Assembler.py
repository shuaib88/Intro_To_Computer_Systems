from Code import Code

class Assembler():

    def __init(self, inputFile):
        pass



# strip white space and comments
for line in inputFile:
    if line.startswith("//"):
        pass

    elif "//" in line:
        line = line.partition('//')[0]
        line = line.rstrip()
        newLine = re.sub(r"[ \t\v\n]", "", line)
        outputFile.write(newLine)

    else:
        if line == "\n" or line == "\r":
            pass
        else:
            newLine = re.sub(r"[ \t\v]", "", line)
            outputFile.write(newLine)

## get symbols


## actually build the correct code


## run