#!/usr/bin/python3
"""
Lists all City objects from a database.
"""

from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State

if __name__ == "__main__":
    """
    Retrieve and display information about City objects from a database.
    """
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.commit()
    # close session
    session.close()
