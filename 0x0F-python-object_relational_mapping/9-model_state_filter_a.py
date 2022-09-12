#!/usr/bin/python3
"""
lists all State objcts that contain the letter 'a' from the db hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqlbd://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()
    for state in states:
        print("{}: {}".format(State.id, State.name))
    session.close()
