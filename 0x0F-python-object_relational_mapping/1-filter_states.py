#!/usr/bin/python3
"""
list all states starting with 'n'
"""

# import module
import MySQLdb
import sys

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Database connection parameters
    host = "localhost"
    port = 3306
    charset = "utf8"
    user = argv[1]
    password = argv[2]
    database = argv[3]

    query = "SELECT id, name FROM states ORDER BY id ASC"

    with MySQLdb.connect(host=host, port=port, charset=charset, user=user, passwd=password, db=database) as conn:
        with conn.cursor() as cur:
            cur.execute(query)

            # Fetch and process data in smaller batches
            batch_size = 100
            while True:
                batch_rows = cur.fetchmany(batch_size)
                if not batch_rows:
                    break
                for row in batch_rows:
                    print(row)
