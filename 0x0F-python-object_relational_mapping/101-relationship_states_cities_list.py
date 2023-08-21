#!/usr/bin/python3
"""list all cities and states"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

def main():
    if len(sys.argv) != 4:
        print("Usage: {} <db_user> <db_password> <db_name>".format(sys.argv[0]))
        return

    db_user, db_password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{db_user}:{db_password}@localhost/{db_name}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        for state in session.query(State).order_by(State.id):
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))
    except Exception as e:
        print("An error occurred:", e)
    finally:
        session.close()

if __name__ == "__main__":
    main()
