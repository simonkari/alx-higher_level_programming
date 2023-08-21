#!/usr/bin/python3
""" This script retrieves and prints states
    whose names start with a capital N from a MySQL database.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database using command-line arguments.
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()

    # Define a SQL query to select states with names that match the provided argument.
    query = """ SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    
    # Execute the query and fetch all the rows that match the criteria.
    cur.execute(query)
    query_rows = cur.fetchall()

    # Iterate through the fetched rows and print each row.
    for row in query_rows:
        print(row)

    # Close the cursor and the database connection.
    cur.close()
    conn.close()
