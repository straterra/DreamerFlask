#!/usr/bin/python

# https://pythonspot.com/login-authentication-with-flask/

# Imports
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from app import *

## Variables
# DB Name
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
Base = declarative_base()

########################################################################


class User(Base):
    """"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    # ----------------------------------------------------------------------
    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password


# Create tables
Base.metadata.create_all(engine)