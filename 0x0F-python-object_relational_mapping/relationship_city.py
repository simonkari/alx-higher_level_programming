#!/usr/bin/python3
"""
This script defines SQLAlchemy model for representing
cities and their states.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
import sqlalchemy


class City(Base):
    """city class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    """
    The name of the city.

    Type: str
    """
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
