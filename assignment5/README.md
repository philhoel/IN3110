# Assignment 5

## Problem 5.1 Syntax Highlighting
Run: python highlighter.py hello.ny naython.syntax naython.theme

## Problem 5.2 Python syntax
Run: python highlighter.py demo.py python.syntax python.theme
### Bonus
Should work for:
- Comment
- String
- Functions
- Operators
- for-loops
- while-loops
- if/elif/else
- Special words/statements: True, False, None
- try/except
- imports

## Problem 5.3 Syntax for favorite language
Language chosen: C++  
Run: python highlighter.py demo.cpp favorite_language.syntax favorite_language.theme

### Bonus
Should work for:
- Comment
- String
- Functions
- For-loops
- While-loops
- if/else
- Special words/statements: true, false
- includes
- throw
- include package name

## Problem 5.4 grep
Run: python grep.py file pattern --highlight  
Example file added: bio.txt  
Example: python grep.py bio.txt [^.]celle --highlight true

Should work as supposed to in non-bonus assignment, with highlight coloring 6 different colors in repeat

## Problem 5.5 Superdiff
Run: python diff.py file1 file2  
Example: python diff.py original.txt modified.txt  
Note: Could not finish this problem. The script works fine for files with the same amounts of lines, but if not then it starts to repeat.  
The basic functions of the scipt is to check line for line if it has been added, removed or modified. See example files.

## Problem 5.6 Color diff
Does not directly follow the assignment. I have simply colored the lines with [+] and [-] in last problem with green and red, respectivly
