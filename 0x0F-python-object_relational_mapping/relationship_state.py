#!/usr/bin/python3
"""
contains the class definition of a State
and an instance Base = declarative_base()
representa the relationship with the class City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import City
from sqlalchemy import relationship


Base = declarative_base()


class State(Base):
    """
    schema for states table in db
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
