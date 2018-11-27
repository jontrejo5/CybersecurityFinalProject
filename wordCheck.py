import string
import re

def wordCheck(searchWord):
    file = open("wordList.txt")
    words = file.read()
    for item in words:
        item = item.lower()
        item = re.sub(r'[^\w\s]', '', item)

    searchWord=str(searchWord).split()
    refinedList=[]

    for word in searchWord:
        word = re.sub(r'[^\w\s]','',word)
        word = word.lower() + "\n"
        if word not in words:
            refinedList.append(word[:-1]+" ")
    return refinedList
