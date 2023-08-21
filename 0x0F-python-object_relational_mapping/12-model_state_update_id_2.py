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
    if len(sys.argv) != 4:
        print("Usage: python script_name.py username password dbname")
        return

    connection_string = (
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    )

    try:
        engine = create_engine(connection_string, pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        with Session() as session:
            state = session.query(State).filter_by(id=2).first()
            if state:
                state.name = "New Mexico"
                session.commit()
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
