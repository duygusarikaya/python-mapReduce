#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None
request = None
hitsForRequest = 0;

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHit = data_mapped

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", hitsTotal
	if hitsForRequest < hitsTotal:
	    hitsForRequest = hitsTotal
	    request = oldKey
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += float(thisHit)

if oldKey != None:
    if hitsForRequest < hitsTotal:
	hitsForRequest = hitsTotal
        request = oldKey
    print request, "\t", hitsForRequest

