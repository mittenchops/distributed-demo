#!/usr/bin/env python

from __future__ import division, print_function
import sys

total = 0
n = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    title, count = line.split('\t', 1)
    n = n + 1
    total = total + int(count)


print("Sum: {}\tn: {}\tAverage: {}".format(total,n,total/n))
