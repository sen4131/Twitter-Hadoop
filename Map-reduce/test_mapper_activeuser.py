#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    username = line.split("\t")[6]
    rate = line.split("\t")[8]
    # write the results to STDOUT (standard output);
    print (username + "\t" + rate)

