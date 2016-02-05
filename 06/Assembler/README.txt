Shuaib's Assembler

My program can be run from any machine that has python 3 and likely python 
2.7 and later

From the command line navigate to the src directory

To run the program use the following replacing testFile.asm with your file
>> python3 Assembler.py /path/testfile.asm

You must write the full path of the testfile in addition to the file name

There is no error handling so you must not pass more arguments than above

You will see the a new file appear in the same directory you passed as path
this will contained compiled hack code that can be run on the CPU emulator

NOTES on construction:
I have a parser module with logic to parse the input file
A code module has dictionaries of binary code maps as well as method to 
access them.RemoveWhiteSpace has code to remove comments and extra whitespace.

I used one outside resource to get the codes for the symbol table instead of hand
coding them. The reference is listed in the appropriate place.
