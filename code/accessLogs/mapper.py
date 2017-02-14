#!/usr/bin/python

# Format of each line is:
# IP\tidentity\tusername\ttime\trequest line\tstatus\tsize
#
# We want elements 4 (request) and hit time
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
    request = request.replace('http://www.the-associates.co.uk','')
    url = request.split(' ')[1]
    if not url:
	continue;
    print "{0}\t{1}".format(url, 1)

