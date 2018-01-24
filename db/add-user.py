#!/usr/bin/python

# Written by Thomas York

# Imports

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_hashing import Hashing
from app.tabledef import *
from app import app
import os
import getpass

# Setup
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'auth.sqlite3'), echo=True)

# Ask user for information
user = raw_input("Username:")
passwd = getpass.getpass("Password for " + user + ":")

h = hashing.hash_value(passwd, salt=app.config['SECRET_KEY'])

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(user, h)
session.add(user)

# commit the record the database
session.commit()

session.commit()
