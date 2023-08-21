#!/usr/bin/python3
'''
A script that selects and displays all states from the database hbtn_0e_0_usa.
'''

import sys
import MySQLdb

def fetch_and_print_states(user, password, database):
    query = "SELECT id, name FROM states ORDER BY id ASC"
    
    with MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=database) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            for row in cur:
                print(row)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    fetch_and_print_states(username, password, database)
