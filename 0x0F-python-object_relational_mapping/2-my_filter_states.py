#!/usr/bin/python3
""" print states starting with capital N"""

#import module
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    query = """ SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY
        states.id ASC"""
    query = query.format(argv[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    # close database connection
    cur.close()
    conn.close()
