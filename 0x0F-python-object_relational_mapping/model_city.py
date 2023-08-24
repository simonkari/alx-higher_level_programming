#!/usr/bin/python3
"""
Contains the class definition of a State and an
instance of Base using declarative_base().
Base = declarative_base()
"""

# Import modules
import sqlalchemy
from sqlalchemy import Column, Integer, String
from model_state import Base
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ City class inheriting from declarative_base() of Base.
    Represents a connection to the MySQL table named 'cities'.
    Attr:
        id, name
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
    """
    The foreign key referencing the associated state's ID.

    Type: int
    """
