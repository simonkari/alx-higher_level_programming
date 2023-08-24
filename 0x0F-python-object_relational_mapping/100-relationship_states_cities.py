#!/usr/bin/python3
"""
A script that inserts a State object into the database.
"""

# Import modules
from relationship_state import Base, State
from relationship_city import City
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    """
    Add the State 'California' with the City 'San Francisco' to the database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")

    new_city = City(name="San Francisco")

    new_state.cities.append(new_city)

    session.add(new_city)

    session.commit()

    # Terminate the session when finished
    session.close()
