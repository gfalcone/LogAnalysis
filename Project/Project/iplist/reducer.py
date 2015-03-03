#!/usr/bin/python

import sys

totalRequests = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisRequest = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", totalRequests
        oldKey = thisKey
        totalRequests = 0

    oldKey = thisKey
    totalRequests += 1

if oldKey != None:
    print oldKey, "\t", totalRequests
