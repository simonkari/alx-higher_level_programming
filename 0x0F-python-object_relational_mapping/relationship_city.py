#!/usr/bin/python3
""" Provide a definition for a city entity."""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """Class representing a city."""
    __tablename__ = "cities"  # This sets the name of the table in the database.
    
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    # The 'id' column serves as the primary key for the 'cities' table.
    
    name = Column(String(128), nullable=False)
    # The 'name' column stores the name of the city, limited to 128 characters.
    
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # The 'state_id' column is a foreign key that references the 'id' column in the 'states' table.
    # This establishes a relationship between cities and states.
