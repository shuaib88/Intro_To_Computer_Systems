#removes whitespace
import re
class RemoveWhitespace:

    #remove white space and Comments from an inputArray and drops into a new array.
    @staticmethod
    def removeWhiteSpaceAndComments(inputArray):
        # the array we will keep our trimmed lines in
        outputArray = []

        # iterate through inputArray
        for line in inputArray:
            if line.startswith("//"):
                pass

            elif "//" in line:
                line = line.partition('//')[0]
                line = line.rstrip()
                newLine = re.sub(r"[ \t\v\n]", "", line)
                outputArray.append(newLine)

            else:
                if line == "\n" or line == "\r":
                    pass
                else:
                    newLine = re.sub(r"[ \t\v\n]", "", line)
                    outputArray.append(newLine)

        return outputArray