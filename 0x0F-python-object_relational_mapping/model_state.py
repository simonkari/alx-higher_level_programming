#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    """ORM class for states."""
    __tablename__ = "states"
    
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True, index=True)  # Add an index for efficiency
    name = Column(String(128), nullable=False)
    
    # If there are relationships to other tables, define them here
    # Example: cities = relationship("City", back_populates="state", lazy="joinedload")
    
    def __repr__(self):
        return f"<State(id={self.id}, name={self.name})>"

# You can add your main code here, which instantiates the session and queries the data.
# Implement batch processing and connection pooling if needed.
