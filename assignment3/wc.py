
import sys
import os


def wordCount(x):
    """
    Takes in a file or multiple to be read and prints out
    number of words,lines and characters and filename
    """
    infile = open(x, "r")
    lineCount = 0
    wc = 0
    charCount = 0
    for line in infile:
        lineCount += 1
        words = line.split()
        wc += len(words)
        for i in words:
            charCount += len(i)

    print(lineCount, wc, charCount, x)


for i in range(1, len(sys.argv)):
    if os.path.isdir(sys.argv[i]):
        continue
    else:
        wordCount(sys.argv[i])