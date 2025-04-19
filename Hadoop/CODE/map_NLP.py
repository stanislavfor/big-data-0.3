#! /usr/bin/env python

#import package
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def mapper():
    
    # initialize sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # transfer each comment to numeric data
    for line in sys.stdin:
        
        # transfer string to python dictionary
        data = eval(line.strip())
        
        # get comment rate
        rate = data['overall']
        
        # get comment
        #summary = data['reviewText']
        summary = data['summary']
        
        # use sentiment analyzer to transfer comment to numeric data
        vs = analyzer.polarity_scores(summary)
        
        # add rate to ditonary
        vs['rate'] = rate
        
        # add reviewer ID as key
        vs['account'] = data['reviewerID']
        
        # pop new numeric data to reducer
        print(vs)
mapper()
