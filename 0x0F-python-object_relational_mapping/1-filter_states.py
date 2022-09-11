#!/usr/bin/python3
"""
 lists all states with a name starting with N (upper N)
 from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    curs = con.cursor()

    curs.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
ORDER BY state.id""")
    states = curs.fetchall()
    for state in states:
        print(state)
    con.close()
