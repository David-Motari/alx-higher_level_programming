#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from model_city import State, City, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2],
                                   argv[3]), pool_pre_ping=True)
    session = Session(bing=engine)
    cities = session.Query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
