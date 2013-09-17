#!/usr/local/bin/python

import cgi
import _mysql
import sys

print "Content-Type: text/html"
print
form = cgi.FieldStorage()

if "checkConflicts" in form:
    numOfPartiers = int(form["numofpartiers"].value)
    partiers = []
    
    for i in range (numOfPartiers):
        if ("partier" + str(i) + "fid") in form:
            newPartier = long(form["partier" + str(i) + "fid"].value)
            partiers.append(newPartier)
    
    import getEnemiesFromSQL as ge
    import findFriendlyGroups as ff

    
    haters = ge.getEnemiesFromSQL()
    friends = ff.findFriendlyGroups(partiers, haters)

    import json

    print json.dumps(friends, sort_keys=True, indent=4, separators=(',', ': '))
