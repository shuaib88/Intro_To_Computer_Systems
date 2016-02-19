Shuaib's VMTranslator

My program can be run from any machine that has python 3 and likely python 
2.7 and later

From the command line navigate to the src directory

To run the program use the following replacing /path with the
full path to your file or directory
>> python3 Assembler.py /path

There is no error handling so you must not pass more arguments than above

You will see the a new file appear in the same directory you passed as path
this will contained assembly code that can be run on the CPU emulator

NOTES on construction:
I have a parser module with logic to parse the input file
A codeWriter module has the logic, text and dictionary to appropriately write code
access them.RemoveWhiteSpace has code to remove comments and extra whitespace.

I used one outside resource to get the codes for the symbol table instead of hand
coding them. The reference is listed in the appropriate place.

ATTRIBUTIONS:
I used the class notes worksheet as a base for most all of my codeWriter code. I used the examples and then built variations off it
Thanks to Marty and Thomas for helping me debug and learn the code