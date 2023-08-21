#!/usr/bin/python3
"""list all states starting with n"""

import MySQLdb
from sys import argv

def main():
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                               user=argv[1], passwd=argv[2], db=argv[3])

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
