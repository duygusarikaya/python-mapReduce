#!/usr/bin/python

# Format of each line is:
# IP\tidentity\tusername\ttime\trequest line\tstatus\tsize
#
# We want elements 0 (ip address) and hit time
# We need to write them out to standard output, separated by a tab

import sys, re

p = re.compile(
    '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
    )
for line in sys.stdin:
    data = line.strip()
    m = p.match(data)
    if not m:
	continue;
    ip, identity, username, date, request, status, size = m.groups()
    print "{0}\t{1}".format(ip, 1)

