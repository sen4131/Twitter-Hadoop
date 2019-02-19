#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

highest_user = None
highest_rate = 0
user = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    
    user, rate = (line.split('\t')[0],line.split('\t')[1])

    # convert count (currently a string) to int
    try:
        rate = int(rate)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if rate > highest_rate:
        highest_rate = rate
        highest_user = user

print (highest_user + '\t' + str(highest_rate))

