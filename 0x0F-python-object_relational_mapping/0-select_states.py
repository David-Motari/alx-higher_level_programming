#!/usr/bin/python3
"""
connecting to the db to make query
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db_con = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db_con.cursor()
    curs.excute("SELECT * FROM `states`;")
    states = curs.fetchall()
    for state in states:
        print(states)
    db_con.close()
