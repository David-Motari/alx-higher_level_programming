#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    srch = argv[4]
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities JOIN
        states ON states.id = cities.state_id WHERE states.name='{:s}'
        ORDER BY cities.id ASC""".format(srch))
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    conn.close()
