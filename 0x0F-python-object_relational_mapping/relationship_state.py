#!/usr/bin/python3
"""
Contains the class definition of a State and an
instance of Base using declarative_base().
Base = declarative_base()
"""

# Import modules
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class inheriting from declarative_base() of Base.
    Represents a connection to the MySQL table named 'states'.
    Attr:
        id, name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    """
    The primary key of the state record.

    Type: int
    """
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade='delete', backref="state")
