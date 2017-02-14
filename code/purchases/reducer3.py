#!/usr/bin/python

import sys

salesTotal = 0
salesCount = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the saleCount, val is the sale amount
#

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisCount, thisSale = data_mapped

    salesCount += float(thisCount)
    salesTotal += float(thisSale)

print salesCount, "\t", salesTotal

