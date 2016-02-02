Shuaib's whitespace and comment remover 

My program can be run from command line on any machine that has python 2.7 or
greater (older versions of python may run, but I haven't tested this)

First navigate to the src directory

To run the program to strip whitespace and keep comments type the following:
>> python stripWhiteSpace.py /path/testfile.in

To run the program to strip whitespace and strip comments type the following: 
>> python stripWhiteSpace.py /path/testfile.in no-comments

In both instances, you must write the full path of the testfile in addition to the file name

A file with too many or too few arguments will return an error message
