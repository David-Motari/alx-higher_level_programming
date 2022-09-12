#!/usr/bin/python3
"""
contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    schema for city table in db
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey('States.id'),)
