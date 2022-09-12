#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bing=engine)
    new_item = State(name="Louisiana")
    session.add(new_item)
    session.commit()
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(new_state.id))
    session.close()
