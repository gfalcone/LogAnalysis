#!/usr/bin/python

import sys

totalNumber = 0
oldKey = None
day = list()
number = list()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNumber = data_mapped

    if oldKey and oldKey != thisKey:
	if len(day) == 0:
		number.append(totalNumber)
		day.append(oldKey)			
	elif len(day) <= 10:
		if totalNumber > number[len(day)-1]:
			for i in range(0,len(day)):
				if i == 0 and totalNumber > number[i]:
					day.insert(0, oldKey)
					number.insert(0,totalNumber)
					day.pop()
					number.pop()
				if i != 0 and totalNumber > number[i] and totalNumber < number[i-1]:
					day.insert(i, oldKey)
					number.insert(i, totalNumber)
					day.pop()
					number.pop()
		elif len(day) < 10 and totalNumber <= number[len(day)-1]:
			day.append(oldKey)
			number.append(totalNumber)
								

        oldKey = thisKey
	totalNumber = 0

    oldKey = thisKey
    totalNumber += 1

if oldKey != None:
	if len(day) == 0:
		number.append(totalNumber)
		day.append(oldKey)			
	elif len(day) <= 10:
		if totalNumber > number[len(day)-1]:
			for i in range(0,len(day)):
				if i == 0 and totalNumber > number[i]:
					day.insert(0, oldKey)
					number.insert(0,totalNumber)
					day.pop()
					number.pop()
				if i != 0 and totalNumber > number[i] and totalNumber < number[i-1]:
					day.insert(i, oldKey)
					number.insert(i, totalNumber)
					day.pop()
					number.pop()
		elif len(day) < 10 and totalNumber <= number[len(day)-1]:
			day.append(oldKey)
			number.append(totalNumber)


for i in range(0, len(day)):
	print day[i], "\t", number[i]



	
