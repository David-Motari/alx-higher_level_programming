#!/usr/bin/python3
"""
connecting to the db to make query
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curs = db_con.cursor()
    curs.execute("SELECT * FROM `states`;")
    states = curs.fetchall()
    for state in states:
        print(states)
    db_con.close()
