#!/usr/bin/python


import sys

totalNumber = 0
oldKey = None
days = 0


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNumber = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey,"\t", totalNumber
	totalNumber = 0
	

    oldKey = thisKey
    totalNumber += 1

if oldKey != None:
    print oldKey, "\t", totalNumber
