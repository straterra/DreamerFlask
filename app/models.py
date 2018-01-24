#!/usr/bin/python

# Written by Thomas York
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

# Imports
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        """"""
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)
