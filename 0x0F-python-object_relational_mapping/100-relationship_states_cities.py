#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco” from
the database hbtn_0e_100_usa: (100-relationship_states_cities.py)
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_city = City(name='San Francisco')
    new_state = State(name='California')
    new.cities.append(new_city)
    session.add_all([new_state, new_city])
    session.commit()
    session.close()
