#!/usr/bin/python

# Format of each line is:
#"id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	
#"abs_parent_id"	"added_at"	"score"	"state_string"	"last_edited_id"	
#"last_activity_by_id"	"last_activity_at"	"active_revision_id"	"extra"	"extra_ref_id"	
#"extra_count"	"marked"
#
# We want element 4 (body)

import sys, string

lineCount = 0;

for line in sys.stdin:
    if lineCount == 0:
	lineCount += 1;
	continue;
    data = line.strip().split('\t');
    if len(data) != 19:
	continue;
    
    idtty, title, tags, author, body, node, parent, abs_parent, added, score, state, edited, activityid, activity,revision, extra, ref, count, marked = data
    body = body.replace('<p>', ' ');
    body = body.strip().translate(None, string.punctuation);
    #print "{0}\t{1}".format(bodyArr, 1);
    bodyData = body.split(' ');
    for word in bodyData:
	if len(word.strip()) > 0:
	    print "{0}\t{1}".format(word, 1);

