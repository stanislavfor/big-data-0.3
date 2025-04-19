#! /usr/bin/env python
# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys

def mapper():
    # read standard input line by line
    for line in sys.stdin:
        # strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")


        # this next line is called 'multiple assignment' in Python
        # this is not really necessary, we could access the data
        # with data[2] and data[5], but we do this for conveniency
        # and to make the code easier to read
        if len(data) == 6:
            date, time, store, item, cost, payment = data

        # Now print out the data that will be passed to the reducer
            print "{0}\t{1}".format(store, cost)


import StringIO
mapper()
