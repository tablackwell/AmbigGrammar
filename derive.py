## Thomas Blackwell          ##
## CSCI Username: tablackw   ##
## tablackwell@email.wm.edu  ##
## CSCI 312 Project Three    ##


## This program, when fed an imput file of a set of rules for a context 
## free grammar, will generate all terminal strings up to given length.
## Arguments must be passed from the command line in the format:       
## python3 derive.py [-lA] B, where A is the integer size of the string,
## and B is the name of the text file containing the grammar.           
## Grammar  rules  must appear  one  rule per line, with each symbol    
## separated from the next symbol by white space ##

import sys
import string
sizeInt = 3 # default value for length of strings to create (3 terminals)
grammarRules = {}
workList = []

## Input Handling ##
## This section checks to see if the length parameter was passed ##
## Otherwise, it will just use the default size of 3. ##
if(len(sys.argv) == 3): # In the case of a size being passed
    grammarSource = str(sys.argv[2]) # Input file to be parsed
    sizeString = sys.argv[1]
    sizeString = sizeString.strip('[]-l')
    if(len(sizeString) == 0): #if there was no number set
        sizeInt = 3
    else:
        sizeInt = int(sizeString[0:]) # Sets the size of our int
else: # If a size is not passed
    grammarSource = str(sys.argv[1])
    
## This block populates grammarRules ##
for line in open(grammarSource, 'r'):
    newRule = line.split()
    production = newRule[2:]
    productionString = ''
    
    if(newRule[0] not in grammarRules.keys()): # Add key if not already a rule
        for item in production:
            productionString = productionString + item + ' '        
        grammarRules[newRule[0]] = [productionString]
        
    else: # Otherwise, add the production to the key's list of values
        for item in production: 
            productionString = productionString + item + ' '
        grammarRules[newRule[0]].append(productionString)
    
startSymbol = open(grammarSource, 'r').readline().split(' ')[0] # get start
workList.append(startSymbol) # Push start symbol to worklist

## Algorithm for generating the strings ##
## Steps of the algorithm are given as inline comments ##
while (len(workList) != 0): # While worklist isn't empty
    
    leftmostNT,itemIndex = '',0 #"item" meaning "leftmost non terminal"
    sentence = workList.pop().split() # Get and delete a potential sentence
    
    if len(sentence) > sizeInt: # Return to top of loop if size out of range
        continue
    
    # Checks for presence of nonterminal, since it would be a key. 
    for item in sentence: 
        if item in grammarRules.keys():
            leftmostNT = item
            itemIndex = sentence.index(item)
            break
    
    # If sentence has no nonterminals, print and return to top of loop    
    if(leftmostNT == ''):
        for item in sentence:
            print(item, end = ' ')
        print()
        continue
    
    # For all productions NT --> RHS
    for value in grammarRules[item]:
        sentenceCopy = []
        
        # Make a copy, replace value of NT with the production
        for item in sentence:
            sentenceCopy.append(item)
        sentenceCopy.remove(leftmostNT)
        sentenceCopy.insert(itemIndex, value)
    
        stringToStore = ''
        
        # Generate a string version of the sentence for ease of manipulation
        for item in sentenceCopy:
            stringToStore = stringToStore + item + ' '
        
        # Push the new sentence to the worklist    
        workList.append(stringToStore)
