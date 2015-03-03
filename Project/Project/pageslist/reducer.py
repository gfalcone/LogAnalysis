#!/usr/bin/python


import sys

totalNumber = 0
oldKey = None



for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNumber = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalNumber
        oldKey = thisKey
        totalNumber = 0

    oldKey = thisKey
    totalNumber += float(thisNumber)

if oldKey != None:
    print oldKey, "\t", totalNumber
