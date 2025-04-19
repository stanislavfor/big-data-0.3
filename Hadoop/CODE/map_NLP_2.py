#! /usr/bin/env python

import sys
import string
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

#create the empty list
train = []
test = []
corpus = []

# set your own training file
for line in open('train', 'r'):
    train_json = eval(eval(json.dumps(line))[:-1])
    train.append(train_json)

#readfile
df = pd.DataFrame.from_dict(train)
train_feature = df.summary
train_label = df.overall
train_fe_tran =train_feature
count_vect = CountVectorizer()

train_fe_tran = count_vect.fit_transform(train_fe_tran) 

tfidf_transformer = TfidfTransformer()
train_fe_tran = tfidf_transformer.fit_transform(train_fe_tran)

model = RandomForestClassifier().fit(train_fe_tran, train_label)

for line in sys.stdin:
    dit = {}
    data = eval(line.strip())
    rate = data['overall']
    summary = pd.Series(data['summary'])
    
    test_fe_tran = count_vect.transform(summary) 
    test_fe_tran = tfidf_transformer.transform(test_fe_tran)

    y_pred = model.predict(test_fe_tran)
    key = str(data['unixReviewTime'])+data['reviewerID']
    key_value = dict({"a":key,"pred":y_pred[0],"true":rate})
    print(key_value)

