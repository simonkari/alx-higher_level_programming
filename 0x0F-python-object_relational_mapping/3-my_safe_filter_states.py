#!/usr/bin/python3
"""List all states that match the given argument with no injection risk."""

import MySQLdb
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: {} <user> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    user, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    
    try:
        conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=user, passwd=password, db=database
        )
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        print("An error occurred:", e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
