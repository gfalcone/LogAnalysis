#!/usr/bin/python


import sys
for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        dc1, dc2, dc3, dc4, dc5, dc6, dc7, dc8, dc9, dc10 = data
        print "{0}\t{1}".format(dc9, 1)

