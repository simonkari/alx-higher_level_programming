#!/usr/bin/python3
""" define city object"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base class for SQLAlchemy models
Base = declarative_base()

class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (sqlalchemy.Column): The city's id.
        name (sqlalchemy.Column): The city's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
