#!/usr/bin/python



import sys
generalURL = "http://www.theassociates.co.uk"
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        dc1, dc2, dc3, dc4, dc5, dc6, dc7, dc8, dc9, dc10 = data
	if generalURL in dc7:
		print "{0}\t{1}".format(dc7[30:], 1)
	else:
        	print "{0}\t{1}".format(dc7, 1)

