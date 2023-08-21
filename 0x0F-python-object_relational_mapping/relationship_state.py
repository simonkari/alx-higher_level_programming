#!/usr/bin/python3
""" Declare ORM entity."""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Object-Relational Mapping (ORM) representation of a state. """
    __tablename__ = "states"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        unique=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("state", cascade="all"),
        single_parent=True)
