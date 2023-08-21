#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument.
"""

# Import modules from the SQLAlchemy library
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create tables in database based on the defined models
    Base.metadata.create_all(engine)
    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).\
        filter(State.name == argv[4]).order_by(State.id).all()
    # Query the State object with the name passed as an argument
    if states:
        print("{}".format(states[0].id))
    else:
        print("Not found")
    # Close session
    session.close()
