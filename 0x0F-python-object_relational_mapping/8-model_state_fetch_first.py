#!/usr/bin/python3
"""
Lists the first State object from a database.
"""

# import module
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create the tables in the database based on the defined models
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        # print information about the state
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # close the session
    session.close()
