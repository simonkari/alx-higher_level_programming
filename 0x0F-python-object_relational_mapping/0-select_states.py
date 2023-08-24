#!/usr/bin/python3
"""
A program that chooses and exhibits all the states from the hbtn_0e_0_usa database.
"""

import sys
import MySQLdb

def main():
    """
    Primary function for fetching and showing all states from the database.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create a database connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    try:
        # Generate a cursor for executing SQL queries
        with db.cursor() as cur:
            # Run an SQL query to fetch all states from the "states" table
            cur.execute("SELECT * FROM states ORDER BY id ASC")

            # Retrieve all rows from the query output
            rows = cur.fetchall()

            # Loop through the rows and display each row
            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        # Terminate the database connection
        db.close()

if __name__ == "__main__":
    main()
