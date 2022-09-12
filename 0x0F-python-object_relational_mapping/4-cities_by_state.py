#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], db=argv[3])
cur = conn.cursor()
cur.execute("""SELECT cities.id, cities.name, states.name FROM cities JOIN
        states ON states.id == cities.state_id ORDER BY cities.id ASC""")
cities = cur.fetchall()
for city in cities:
    print(city)
cur.close()
conn.close()
