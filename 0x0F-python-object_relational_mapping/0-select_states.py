#!/usr/bin/python3
'''
A program that chooses and exhibits all the states from the hbtn_0e_0_usa database.
'''

# Import modules
import MySQLdb
import sys

if __name__ == "__main__":
    '''
    Primary script for fetching and displaying all states from the database.
    '''
    # Create a database connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Generate a cursor for executing SQL queries
    cur = db.cursor()
    # Run an SQL query to fetch all states from the "states" table
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Retrieve all rows from the query output
    rows = cur.fetchall()
    # Loop through the rows and display each row
    for row in rows:
        print(row)
    # Terminate the database connection
    cur.close()
    db.close()