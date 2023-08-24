#!/usr/bin/python3
"""
This script establishes an SQLAlchemy model to represent states.
"""

# Import modules
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ State class inheriting from the declarative_base() of Base.
    Represents a connection to the MySQL table named 'states'.
    Attr:
        id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(128), nullable=False)
