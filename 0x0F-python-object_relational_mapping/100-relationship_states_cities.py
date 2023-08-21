#!/usr/bin/python3
"""relationship California and SF"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City


if __name__ == "__main__":
    # Create a database engine using SQLAlchemy's create_engine function
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )
    
    # Create tables in the database based on the defined models
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create and add a new State object
    add_state = State(name="California")
    session.add(add_state)
    session.commit()

    # Create and add a new City object associated with the added State
    add_city = City(name="San Francisco", state_id=add_state.id)
    session.add(add_city)
    session.commit()

    # Close the session when done
    session.close()
