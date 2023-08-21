#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for states.
"""

# import models from sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ORM class for states."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True, doc="Primary key of the state.")
    name = Column(String(128), nullable=False, doc="Name of the state.")
    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"
