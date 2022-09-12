#!/usr/bin/python3
"""
prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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
    s = argv[4]
    state = session.Query(State).filter(State.name == s).\
        order_by(State.id).first()
    if state:
        print("{}".format(str(state.id))
    else:
        print("Not found")
    session.close()
