#!/usr/bin/python3
"""
connecting to the db to make query
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    con = MySQLdb.connect(port=3304, host='localhost',
                          user=argv[1], passwd=argv[2], db=argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
    con.close()
