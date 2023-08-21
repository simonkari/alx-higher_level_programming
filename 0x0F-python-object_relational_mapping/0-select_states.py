#!/usr/bin/python3
'''
A script that selects and displays all states from the database hbtn_0e_0_usa.
'''

# import module
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    
    # Create a cursor to interact with the database
    cur = db.cursor()
    
    # Execute a SELECT query to retrieve data from the "states" table
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    # Fetch all rows returned by the query
    query_rows = cur.fetchall()
    
    # Iterate through the query results and print each row
    for row in query_rows:
        print(row)
    
    # Close the cursor and the database connection
    cur.close()
    db.close()
