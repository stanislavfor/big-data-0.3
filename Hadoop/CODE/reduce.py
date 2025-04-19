#! /usr/bin/env python
import sys

#initial the value
salesTotal = 0
oldKey = None

#receive the data and run the loop
for line in sys.stdin:
    #split the word
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue
    #assign the parameter
    thisKey, thisSale = data
    
    #compare the oldkey and newkey
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey
        salesTotal = 0
    
    #increment the total sale
    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal
                                  
