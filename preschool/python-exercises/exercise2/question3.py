# script for solution to question 3 of exercise 2

# python imports
import numpy as np
from collections import OrderedDict

string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# direct approach using numpy
print("Count chart for letters in string using numpy: ")
print("=========================================")
unique, counts = np.unique(list(string), return_counts=True)    # get letter frequency
print(*[f"{val}: {freq}" for val, freq in zip(unique, counts)], sep="\n")

# indirect approach using dict
print("Count chart for letters in string using dictionary: ")
print("==================================================")
letterDict = {} # initialise dictionary
for letter in string:
    if not letter in letterDict:
        letterDict[letter] = 0
    letterDict[letter] += 1 # increment letter count
letterDict = OrderedDict(sorted(letterDict.items()))    # sort dictionary
print(*[f"{letter}: {letterDict[letter]}" for letter in letterDict], sep="\n")
