#!/usr/bin/python3
"""
This script retrieves and displays rows from the 'states'
table of the 'hbtn_0e_0_usa' database where the 'name'
column matches the provided argument.
"""

# import module
import MySQLdb
from sys import argv

if __name__ == "__main__":

    """
    Main script to retrieve and display rows from the 'states' table.
    """
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith("N"):
            print(row)
    cur.close()
    conn.close()
