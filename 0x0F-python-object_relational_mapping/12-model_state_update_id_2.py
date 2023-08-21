#!/usr/bin/python3
"""
Changes the name of the State object with id=2 to 'New Mexico'.
"""

# Import modules from the SQLAlchemy
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.id == 2).all()
    if states:
        # Update the name of the State
        states[0].name = "New Mexico"
    session.commit()
    # close session
    session.close()
