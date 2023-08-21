#!/usr/bin/python3
"""
Lists all State objects.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    try:
        engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        with Session() as session:
            states = session.query(State).order_by(State.id).all()
            for state in states:
                print(f"{state.id}: {state.name}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()
