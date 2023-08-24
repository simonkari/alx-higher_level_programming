#!/usr/bin/python3
"""Script that lists all objects from a database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sqlalchemy
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """
    Display all State instances stored in a database.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    #Generate the database tables according to the specified models
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for states_id, states_name in session.query(State.id,
                                                State.name).order_by(State.id):
        print("{}: {}".format(states_id, states_name))
