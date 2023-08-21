#!/usr/bin/python3
"""
 SQLAlchemy model for representing
cities and their associated states.
"""

# Import necessary modules
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# Create a base class for declarative models
Base = declarative_base()

# Define the City class, inheriting from the Base class
class City(Base):
    """city class"""
    __tablename__ = "cities"
    
    # Define attributes/columns of the City class
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
