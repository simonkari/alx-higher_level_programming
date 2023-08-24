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
    """ 
    This class serves as an SQLAlchemy model, outlining
    the structure and characteristics of a state.

    Attributes:
        __tablename__ (str): The name of the database table
            where state records are stored.

        id (int): The primary key for state records.
        name (str): The name of the state.

    Note:
        The class definition establishes a mapping of
        this model to the "states" table in the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String(128), nullable=False)
