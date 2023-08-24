#!/usr/bin/python3
"""Script that lists all objects from a database
"""

# Import the modules
import sys
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """
    Fetch and exhibit all State and associated City objects
    from the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    #Present details regarding each State object and its associated entities
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    #Terminate the session when finished
    session.close()
