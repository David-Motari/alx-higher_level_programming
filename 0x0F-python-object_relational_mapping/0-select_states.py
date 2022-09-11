#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """
    connecting to the db to make query
    """
    try:
        db_con = MySQLdb.connect(
                user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        curs = db_con.cursor()
        curs.excute("SELECT * FROM `states`;")
        states = curs.fetchall()
        for state in states:
            print(states)
        db_con.close()
    except FileNotFoundError:
        print("Can't connect to database")
        return 0


if __name__ == "__main__":

    main()
