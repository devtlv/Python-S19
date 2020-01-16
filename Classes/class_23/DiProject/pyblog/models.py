#!/usr/local/bin/python3
#
# models.py
# pyblog
#

from pyblog import db

class User(db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64))
    age     = db.Column(db.Integer)
    pwd     = db.Column(db.String(64))



