#!/usr/bin/python3
"""
connecting to the db to make query
filter with name starting with 'N'
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curs = db_con.cursor()
    curs.execute("SELECT * FROM states
                 WHERE state.name LIKE BINARY 'N%'
                 ORDER BY state.id")
    states = curs.fetchall()
    for state in states:
        print(state)
    db_con.close()
