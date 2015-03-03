#!/usr/bin/python

import sys


totalNumber = 0
oldKey = None
ip = list()
number = list()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNumber = data_mapped

    if oldKey and oldKey != thisKey:
	if len(ip) == 0:
		number.append(totalNumber)
		ip.append(oldKey)			
	elif len(ip) <= 10:
		if totalNumber > number[len(ip)-1]:
			for i in range(0,len(ip)):
				if i == 0 and totalNumber > number[i]:
					ip.insert(0, oldKey)
					number.insert(0,totalNumber)
					ip.pop()
					number.pop()
				if i != 0 and totalNumber > number[i] and totalNumber < number[i-1]:
					ip.insert(i, oldKey)
					number.insert(i, totalNumber)
					ip.pop()
					number.pop()
		elif len(ip) < 10 and totalNumber <= number[len(ip)-1]:
			ip.append(oldKey)
			number.append(totalNumber)
								

        oldKey = thisKey
	totalNumber = 0

    oldKey = thisKey
    totalNumber += 1

if oldKey != None:
	if len(ip) == 0:
		number.append(totalNumber)
		ip.append(oldKey)			
	elif len(ip) <= 10:
		if totalNumber > number[len(ip)-1]:
			for i in range(0,len(ip)):
				if i == 0 and totalNumber > number[i]:
					ip.insert(0, oldKey)
					number.insert(0,totalNumber)
					ip.pop()
					number.pop()
				if i != 0 and totalNumber > number[i] and totalNumber < number[i-1]:
					ip.insert(i, oldKey)
					number.insert(i, totalNumber)
					ip.pop()
					number.pop()
		elif len(ip) < 10 and totalNumber <= number[len(ip)-1]:
			ip.append(oldKey)
			number.append(totalNumber)


for i in range(0, len(ip)):
	print ip[i], "\t", number[i]



	
