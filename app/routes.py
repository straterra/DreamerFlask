#!/usr/bin/python

# Written by Thomas York
from app import app
from app import hashing

# Imports
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from sqlalchemy.orm import sessionmaker
from flask_hashing import Hashing
from app.tabledef import *
import os

# Routes
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        return "Hello Boss!<br \><br \><a href=\"/logout\">Logout</a>"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":

        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]))
        result = query.first()
        passwd = result.password

        if hashing.check_value(passwd, POST_PASSWORD, salt=app.config['SECRET_KEY']):
            session['logged_in'] = True
            return redirect('/')
        else:
            flash('wrong password!')
            return redirect('/login')
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()