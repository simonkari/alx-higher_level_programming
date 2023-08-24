#!/usr/bin/python3
"""Contains the class definition of a State and an
instance of Base using declarative_base(). """


import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ State Class inheriting from Base using declarative_base().
    Represents a link to the MySQL table 'states'.
    
    Attributes:
        id: The ID of the state.
        name: The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
