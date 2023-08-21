#!/usr/bin/python3
""" add a new city class, print cities"""

# Import modules
import sqlalchemy
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # Create a database engine using MySQL dialect
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Create the necessary database tables
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)
    # Create a session instance
    session = Session()
    
    # Query cities and their corresponding states
    fetch = session.query(City, State).\
        filter(City.state_id == State.id).all()
    
    # Iterate through the query results and print them
    for city, state in fetch:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    
    # Commit the changes made during the session
    session.commit()
    # Close the session
    session.close()
