#!/usr/local/bin/python

import cgi
import _mysql

print "Content-Type: text/html"
print 
form = cgi.FieldStorage()

if "user_fid" in form:
    if "disliker_fid" in form:
        if "disliked_fid" in form:
            user = str(long(form["user_fid"].value))
            disliker = str(long(form["disliker_fid"].value))
            disliked = str(long(form["disliked_fid"].value))
            con = _mysql.connect('transfixed.db', 'evilseanbot', 'sqlisforsuckers', 'ballofhate')
            query = "INSERT INTO dislikes VALUES ('', " + disliker+ ", " + disliked + ", " + user + ")"
            con.query(query)
            con.use_result()
            con.close()
            print "Entry inserted"
else:
    print "Nothing to report!"
