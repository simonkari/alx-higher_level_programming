#!/usr/bin/python3
"""Represents a state in the database."""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


Base = declarative_base()


class State(Base):
    """
Describes a state entity within a MySQL database.

Attributes:
    __tablename__ (str): The name of the table storing state records.
    id (sqlalchemy.Integer): The unique identifier of the state.
    name (sqlalchemy.String): The name of the state.
    cities (sqlalchemy.orm.relationship): Relationship with associated cities.
"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
