#!/usr/bin/python3
"""
A script takes in the name of a state as an argument
and lists all cities of that state, by use of the database hbtn_0e_4_usa.
"""

# import module
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        with MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                             user=argv[1], passwd=argv[2], db=argv[3]) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT cities.name FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;
                """, (argv[4],))
            cities = [city[0] for city in cur.fetchall()]
            print(", ".join(cities))
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
