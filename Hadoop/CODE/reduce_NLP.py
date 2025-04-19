#! /usr/bin/env python

import pandas as pd
import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

#function to count each value in data
def countnum(test, pred):
        ctr1 = 0        #counter for 1 occur
        ctr1T = 0       #counter for 1 that preditive correct
        ctr2 = 0        #counter for 2 occur
        ctr2T = 0       #counter for 2 that preditive correct
        ctr3 = 0        #counter for 3 occur
        ctr3T = 0       #counter for 3 that preditive correct
        ctr4 = 0        #counter for 4 occur
        ctr4T = 0       #counter for 4 that preditive correct
        ctr5 = 0        #counter for 5 occur
        ctr5T = 0       #counter for 5 that preditive correct

        merge = pd.concat([test, pred], axis=1)         #merge the test value and pred value
        np_merge = np.array(merge)

        for i in range(len(np_merge)):
                if np_merge[i][0] == 1:
                        ctr1 = ctr1 + 1
                        if np_merge[i][0] == np_merge[i][1]:
                                ctr1T = ctr1T + 1
                elif np_merge[i][0] == 2:
                        ctr2 = ctr2 + 1
                        if np_merge[i][0] == np_merge[i][1]:
                                ctr2T = ctr2T + 1
                elif np_merge[i][0] == 3:
                        ctr3 = ctr3 + 1
                        if np_merge[i][0] == np_merge[i][1]:
                                ctr3T = ctr3T + 1
                elif np_merge[i][0] == 4:
                        ctr4 = ctr4 + 1
                        if np_merge[i][0] == np_merge[i][1]:
                                ctr4T = ctr4T + 1
                elif np_merge[i][0] == 5:
                        ctr5 = ctr5 + 1
                        if np_merge[i][0] == np_merge[i][1]:
                                ctr5T = ctr5T + 1
        return ctr1T/float(ctr1), ctr2T/float(ctr2), ctr3T/float(ctr3), ctr4T/float(ctr4), ctr5T/float(ctr5)


# initialize
rates = []
trains = []

# set how many line you want to set as test data
n = 10000

# get each line data
# transfer data to list
for line in sys.stdin:
    rate_data = eval(line)
    rate = rate_data.pop("rate")
    viewid = rate_data.pop("account")
    value = rate_data.values()


    # append all the rate and value to form whole list
    rates.append(rate)
    trains.append(value)

# transfer all the data to numpy array
x = np.array(trains)
y = np.array(rates)

# set traning test data base on n
train_x = x[:-n,:]
test_x = x[-n:,:]

train_y = y[:-n]
test_y = y[-n:]


# use random forest to train the data
rf = RandomForestClassifier()
rf.fit(train_x, train_y)

# get predict rate
y_pred = rf.predict(test_x)

# get the accuracy between ture rate and predict rate
score = metrics.accuracy_score(test_y,y_pred)
matrix = metrics.confusion_matrix(true,pred)

# change the format of ture rate and predict rate
ypred = pd.DataFrame(y_pred)
testy = pd.DataFrame(test_y)

# get the accuracy for each value 
acc1, acc2, acc3, acc4, acc5 = countnum(testy, ypred)

print(matrix)

# save score as ouput
print("The final accurary is "+ format(score, '0.3f'))
