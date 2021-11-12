import re
import argparse
import sys

def regexFile(textfile, pattern):
    """
    Reads a file and a regex pattern
    Appends the lines it finds into a list and returns it
    """

    found_regex = []

    text = open(textfile, 'r')
    File = open(textfile, 'r')
    text = text.read()
    regex = re.search(pattern, text)
    if regex is not None:
        for line in File:
            if regex.group(0) in line:
                found_regex.append(line)

    return found_regex

def highlight(list_of_lines):
    """
    Takes in a list
    Loops through the list and adds color codes
    """
    colorLines = []
    i = 1
    color = f'0;3{i}'
    for line in list_of_lines:
        color = f'0;3{i}'
        line = f"\033[{color}m{line}\033[0m"
        colorLines.append(line)
        i += 1
        if i == 7:
            i = 1

    return colorLines


parser = argparse.ArgumentParser(description='Grep: Returns lines that matches pattern')
parser.add_argument('textfile', help='name of textfile')
parser.add_argument('pattern', help='A regex pattern')
parser.add_argument('--highlight', help='Colors the lines found')
args = parser.parse_args()

grepList = regexFile(args.textfile, args.pattern)
if args.highlight == None:
    if len(grepList) == 0:
        print(f"No matches found for {pattern}")
    else:
        for i in grepList:
            print(i)
else:
    if len(grepList) == 0:
        print(f"No matches found for {pattern}")
    else:
        new_grepList = highlight(grepList)
        for i in new_grepList:
            print(i)