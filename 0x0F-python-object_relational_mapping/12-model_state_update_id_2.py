#!/usr/bin/python3
"""
A script that inserts the State object "Louisiana" into the hbtn_0e_6_usa database.
"""
# Import modules
from model_state import Base, State
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.id == "2").\
        update({State.name: "New Mexico"})
    session.commit()
