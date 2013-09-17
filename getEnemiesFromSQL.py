#!/usr/local/bin/python

import cgi
from sets import ImmutableSet
import MySQLdb as mdb

def getEnemiesFromSQL():
    enemies = []
    con = mdb.connect('transfixed.db', 'evilseanbot', 'sqlisforsuckers', 'ballofhate')
    cur = con.cursor()
    cur.execute("SELECT * FROM dislikes")
    row = cur.fetchone()
    while row is not None:
        newEnemy = [long(row[1]), long(row[2])]
        enemies.append(newEnemy)		
        row = cur.fetchone()		
    con.close()
    return enemies