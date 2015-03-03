#!/usr/bin/python

import sys

totalNumber = 0
oldKey = None
page = list()
number = list()

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNumber = data_mapped

    if oldKey and oldKey != thisKey:
	if len(page) == 0:
		number.append(totalNumber)
		page.append(oldKey)			
	elif len(page) <= 10:
		if totalNumber > number[len(page)-1]:
			for i in range(0,len(page)):
				if i == 0 and totalNumber > number[i]:
					page.insert(0, oldKey)
					number.insert(0,totalNumber)
					page.pop()
					number.pop()
				if i != 0 and totalNumber > number[i] and totalNumber < number[i-1]:
					page.insert(i, oldKey)
					number.insert(i, totalNumber)
					page.pop()
					number.pop()
		elif len(page) < 10 and totalNumber <= number[len(page)-1]:
			page.append(oldKey)
			number.append(totalNumber)
								

        oldKey = thisKey
	totalNumber = 0

    oldKey = thisKey
    totalNumber += 1

if oldKey != None:
	if len(page) == 0:
		number.append(totalNumber)
		page.append(oldKey)			
	elif len(page) <= 10:
		if totalNumber > number[len(page)-1]:
			for i in range(0,len(page)):
				if i == 0 and totalNumber > number[i]:
					page.insert(0, oldKey)
					number.insert(0,totalNumber)
					page.pop()
					number.pop()
				if i != 0 and totalNumber > number[i] and totalNumber < number[i-1]:
					page.insert(i, oldKey)
					number.insert(i, totalNumber)
					page.pop()
					number.pop()
		elif len(page) < 10 and totalNumber <= number[len(page)-1]:
			page.append(oldKey)
			number.append(totalNumber)


for i in range(0, len(page)):
	print page[i], "\t", number[i]



	
