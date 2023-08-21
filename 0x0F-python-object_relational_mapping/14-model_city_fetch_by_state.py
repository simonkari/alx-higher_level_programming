#!/usr/bin/python3
""" add a new city class, print cities"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from model_state import Base, State
from model_city import City

def main():
    db_url = URL(
        drivername='mysql+mysqldb',
        username=argv[1],
        password=argv[2],
        host='localhost',
        port=3306,
        database=argv[3]
    )

    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    
    with Session() as session:
        fetch = session.query(City, State).join(State, City.state_id == State.id).all()
        for city, state in fetch:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.commit()

if __name__ == "__main__":
    main()
