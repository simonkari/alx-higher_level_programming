#!/usr/bin/python3
"""
Lists all State objects.
"""

from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

def establish_connection(username, password, database):
    connection_string = f"mysql+mysqldb://{username}:{password}@localhost/{database}"
    engine = create_engine(connection_string)
    return engine

def list_states(session):
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

def main():
    try:
        username = argv[1]
        password = argv[2]
        database = argv[3]

        engine = establish_connection(username, password, database)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        list_states(session)

        session.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
