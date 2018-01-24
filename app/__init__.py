#!/usr/bin/python

# Written by Thomas York

# Imports
from flask import Flask
from flask_hashing import Hashing
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Flask Setup
app = Flask(__name__)
app.config.from_object(Config)
hashing = Hashing(app)
db = SQLAlchemy(app)

# Route setup
from app.routes import *

# Flask Setup
if __name__== "__main__":
    app.run()