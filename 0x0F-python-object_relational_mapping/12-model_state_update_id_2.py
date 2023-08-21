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

def main():
    # Unpack command line arguments
    script_name, db_user, db_password, db_name = argv
    # Use an f-string for more readable string formatting
    db_url = f"mysql+mysqldb://{db_user}:{db_password}@localhost:3306/{db_name}"
    # Use context manager to handle session and engine
    with create_engine(db_url, pool_pre_ping=True).connect() as engine:
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        # Use .first() to retrieve a single result instead of .all() and indexing
        state = session.query(State).filter(State.id == 2).first()

        if state:
            state.name = "New Mexico"

        session.commit()
    # The session is automatically closed at the end of the context block
if __name__ == "__main__":
    main()
