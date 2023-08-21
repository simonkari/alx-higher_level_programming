#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as an argument.
# Safe from SQL injections.
# Usage: ./3-my_safe_filter_states.py <mysql username> \
#                                     <mysql password> \
#                                     <database name> \
#                                     <state name searched>
import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name> <state name searched>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database)
        c = db.cursor()
        query = "SELECT * FROM `states` WHERE name = %s"
        c.execute(query, (state_name,))
        
        for state in c.fetchall():
            print(state)
        
    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    main()
