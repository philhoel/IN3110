import re
import sys
import argparse


#########################
"""
Syntax highlighter: highlighter.py
Takes in syntaxfile to read what to color
Takes in themefile to read what color to use
"""
#########################


def readFile(syntax, theme):
    """
    Reads in the syntaxfile and themefile
    Splits regex and what the regex finds into a dictionary
    Splits what the regex finds and color code into another dictionary
    """
    themeDict = {}
    syntaxDict = {}

    syntaxFile =  open(syntax, 'r')
    for line in syntaxFile:
        line = line.strip()
        syntaxlines = line.split(": ")
        regex = syntaxlines[0]
        regex = re.sub('\A"|"\Z', '', regex)
        syntaxDict[regex] = syntaxlines[1]


    themeFile = open(theme, 'r')
    for line in themeFile:
        themelines = line.split(':')
        themeDict[themelines[0]] = themelines[1].strip()
        #print(themeDict)

    return syntaxDict, themeDict

def highlighter(input_file, syntax, theme):
    """
    Takes a file to highlight
    Takes a syntaxfile
    Takes a themefile
    Runs readFile() with the syntax and theme files
    Loops through dictionaries and the input file and adds color codes
    """


    syntaxDict, themeDict = readFile(syntax, theme)

    file = open(input_file, 'r')
    text = file.read()


    for key in syntaxDict:
        start_code = f"\033[{themeDict[syntaxDict[key]]}m"
        end_code = "\033[0m"
        text = re.sub(rf'({key})', rf"{start_code}\1{end_code}", text)


    print(text)


parser = argparse.ArgumentParser(description='Highlighter')
parser.add_argument('textfile', help='File to be colored')
parser.add_argument('syntaxfile', help='File containing what syntax should be colored')
parser.add_argument('themefile', help='File containting what color different syntax should be colored')
args = parser.parse_args()

highlighter(args.textfile, args.syntaxfile, args.themefile)
