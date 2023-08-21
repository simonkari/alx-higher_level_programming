#!/usr/bin/python3
"""Print states starting with capital N"""

# import module
import MySQLdb
from sys import argv

def main():
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                               user=argv[1], passwd=argv[2], db=argv[3])

        with conn.cursor() as cur:
            query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
            search_string = argv[4]
            cur.execute(query, (search_string,))
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
