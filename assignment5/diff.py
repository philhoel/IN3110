import re
import argparse

def LineSearch(file1, file2):
    """
    Loops through files and checks if lines are similar
    """

    text = []

    FirstFileDict = {}
    SecondFileDict = {}
    firstFile = open(file1, 'r')
    secondFile = open(file2, 'r')

    i = 0
    for line in firstFile:
        FirstFileDict[i] = line
        i += 1
    FirstFileDictLength = i

    i = 0
    for line in secondFile:
        SecondFileDict[i] = line
        i += 1
    SecondFileDictLength = i

    WordCount = 0
    for Akey in FirstFileDict:
        for Bkey in SecondFileDict:
            if FirstFileDict[Akey][-3:] == "[x]":
                continue
            elif SecondFileDict[Bkey][-3:] == "[x]":
                continue
            else:
                if FirstFileDict[Akey] == SecondFileDict[Bkey]:
                    FirstFileDict[Akey] = "[0] "+FirstFileDict[Akey]
                    text.append(FirstFileDict[Akey])
                    FirstFileDict[Akey] = f"{FirstFileDict[Akey]} [x]"
                    SecondFileDict[Bkey] = f"{SecondFileDict[Bkey]} [x]"
                elif FirstFileDict[Akey] != SecondFileDict[Bkey]:
                    Check_words1 = FirstFileDict[Akey].split()
                    Check_words2 = SecondFileDict[Bkey].split()
                    WordsLength = len(Check_words1)
                    for i in Check_words1:
                        for j in Check_words2:
                            if i == j:
                                WordCount += 1
                    if WordCount >= 0.5*WordsLength:
                        text.append("[-] "+FirstFileDict[Akey])
                        FirstFileDict[Akey] = f"{FirstFileDict[Akey]} [x]"
                        text.append("[+] "+SecondFileDict[Bkey])
                        SecondFileDict[Bkey] = f"{SecondFileDict[Bkey]} [x]"
                    else:
                        text.append("[+] "+SecondFileDict[Bkey])
                        SecondFileDict[Bkey] = f"{SecondFileDict[Bkey]} [x]"



    
    for i in range(len(text)):
        if text[i][:3] == "[0]":
            continue
        elif text[i][:3] == "[+]":
            text[i] = f"\033[0;32m{text[i]}\033[0m"
        elif text[i][:3] == "[-]":
            text[i] = f"\033[0;31m{text[i]}\033[0m"
        else:
            print("Some error has occured")

    for i in text:
        print(i)


parser = argparse.ArgumentParser(description='Grep: Returns lines that matches pattern')
parser.add_argument('file1', help='name of first file')
parser.add_argument('file2', help='name of second file')
args = parser.parse_args()

LineSearch(args.file1, args.file2)


