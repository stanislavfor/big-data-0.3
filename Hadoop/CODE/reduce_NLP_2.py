#! /usr/bin/env python

import pandas as pd
import numpy as np
import sys
from sklearn import metrics


# initiate the list
pred = []
true = []

for line in sys.stdin:
    
    # get the dictionary
    data = eval(line)
    #print(data)
    
    viewid = data.pop("a")
    p = data.pop("pred")
    t = data.pop("true")

    
    #append the value into list
    pred.append(p)
    true.append(t)


# output the accuracy and confusion matrix
score = metrics.accuracy_score(true,pred)
matrix = metrics.confusion_matrix(true,pred)
print(score)
print(matrix)
