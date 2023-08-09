import re
import os

#opening the dictionary file
dictfile = open('./fulldictionary.txt')
dictionary = dictfile.read()

#turning the strings to list of strings
wordslist = dictionary.split()

print('What is the word you are looking for\nlooks like?')
text = input()

#turning user input into regex pattern on a list
letters = []
for i in text:
    if i == ' ':
        letters.append('\w')
    else:
        letters.append(i.upper())

#joining the pattern from the list        
pattern = ''.join(letters)

'''filtering the dictionary to only have
words with same length as pattern
'''
wordlength = len(letters)
potwordslist = []
for i in wordslist:
    if len(i) <= wordlength:
        potwordslist.append(i)

potentialwords = '\n'.join(potwordslist)
  
wordsregex = re.compile(pattern)
words = wordsregex.findall(potentialwords)

if len(words) == 0:
    print('No match found. Try again!')
else:
    print('Here are the matches:')
    for i in words:
        print(' '+i)
                
