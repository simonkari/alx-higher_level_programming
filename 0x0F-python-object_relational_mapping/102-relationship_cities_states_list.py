#!/usr/bin/python3
"""
Lists all City objects.
"""

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State

if __name__ == "__main__":
    """
    Retrieve and display information about City objects.
    """
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    #create session
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()

    #Display the information about cities
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.commit()
    # close session
    session.close()
