import json
from difflib import get_close_matches
file=json.load(open("Dictionary.json","r"))

def findme(m):
    New={k.lower(): v for k, v in file.items()}
    alpha=get_close_matches(m,New.keys(),n=1)
    if m in New:
        to_print=""
        for i in New[m]:
            to_print=to_print+i+"\n"
        return "\n"+to_print
    elif (len(alpha) ==1):
        print("is the correct word is "+ alpha[0].upper())
        for i in range(3):
            try:
                Newword=int(input("press 0 for No or for yes press 1: "))
                if Newword is 1:
                    return findme(alpha[0])
                elif Newword is 0:
                    return "plz Start from startinng?"
                else:
                    if i==2:
                        return "limit excised plz start from Starting"
                    else:
                        print("Plz provide proper input")
                        continue
            except ValueError:
                if i==2:
                    return "limit excised plz start from Starting"
                else:
                    print("Plz enter proper input next time")
                    continue
    else:
        return"bhai ji kya krti aap shi word to daaliye ji .. please provide correct input"

datainput =input("Enter the word to find out: ")
datainput =datainput.lower()
print(findme(datainput))
