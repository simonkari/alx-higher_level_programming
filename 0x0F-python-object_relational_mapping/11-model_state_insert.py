#!/usr/bin/python3
"""
Adds the State object Louisiana to a database and prints its assigned ID.
"""

# Import modules from SQLAlchemy library
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Creating a database engine using the provided MySQL credentials
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Creating tables defined in the model_state module if they don't exist
    Base.metadata.create_all(engine)

    # Creating a session class for interacting with the database
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Creating a new State object and adding it to the session
    add_state = State(name="Louisiana")
    session.add(add_state)
    
    # Committing the changes to the database
    session.commit()
    
    # Printing the ID of the newly added state
    print(add_state.id)
    
    # Closing the session
    session.close()
