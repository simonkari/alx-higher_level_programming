#!/usr/bin/python3
"""
This script is used to select cities by states from the
database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        with MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                             user=argv[1], passwd=argv[2], db=argv[3]) as conn:
            cur = conn.cursor()
            cur.execute("""
                SELECT cities.id, cities.name, states.name FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
                """)
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
