#!/usr/bin/python

import sys

nodes = "";
oldKey = None;
count = 0;

# Loop around the data
# It will be in the format key\tval
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNode = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", count, "\t", nodes
        oldKey = thisKey;
        nodes = "";
	count = 0;

    oldKey = thisKey
    nodes += thisNode + ', ';
    count += 1;

if oldKey != None:
    print oldKey, "\t", count, "\t", nodes

