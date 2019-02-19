#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    field = line.split("\t")[2]
    # split the line into words
    words = field.split()
    # increase counters
    for i in range(len(words)-1):
        # write the results to STDOUT (standard output);
	bigram = words[i]+'::'+words[i+1]
        print '%s\t%s' % (bigram, 1)

