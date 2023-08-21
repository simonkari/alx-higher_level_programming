#!/usr/bin/python3
"""
Defines a SQLAlchemy model for representing
states and their cities.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import sqlalchemy

Base = declarative_base()


class State(Base):
    """ ORM class for state """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
