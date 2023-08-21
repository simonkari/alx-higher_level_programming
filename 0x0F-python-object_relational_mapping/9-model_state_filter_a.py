#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'.
"""

# import module from sqlalchemy
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    List all State objects that contain the letter 'a' from a database.
    """
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    # Iterate through the queried State objects
    for state in session.query(State).\
            filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    # close session
    session.close()
