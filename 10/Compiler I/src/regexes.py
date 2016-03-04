
## this regex matches a comment that take the form
## 1) /* comment until closing */ ,
## 2) /** api comment */,
## 3) // comment to end of line.
comment = r'(?:(?:\/\*\*(?:.|\n)*?\*\/)|(?:\/\/[^\n]*\n))'

# r makes escaping easy \ for example



## this regex matches a string that is identified by " "
string = r'(?:"[^"]*["])|(?:\'[^\']*[\'])'


## this regex i don't really know how it works but it gives me a nice output
delimiters = r'[\(\)\[\]\{\}\,\;\=\.\+\-\*\/\&\|\~\<\>]|'+string+'| *'