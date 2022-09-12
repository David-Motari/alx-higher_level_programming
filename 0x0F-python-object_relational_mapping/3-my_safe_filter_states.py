#!/usr/bin/python3
"""
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    srch = argv[4]
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        if state[1] == srch:
            print(state)
    cur.close()
    conn.close()
