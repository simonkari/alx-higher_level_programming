#!/usr/bin/python3
"""list all states"""

import sys
import MySQLdb

def main():
    '''
    Main script to retrieve and display
    '''
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )

        with db.cursor() as cur:
            # Execute SQL query
            cur.execute("SELECT * FROM states ORDER BY id ASC")

            # Fetch all rows
            rows = cur.fetchall()

            for row in rows:
                print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()
