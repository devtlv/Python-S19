#!/usr/local/bin/python3
#
# models.py
# pyblog
#

import datetime
from pyblog import db, login_mgr
import flask_login

@login_mgr.user_loader
def load_user(userid):
    userid = int(userid)
    return User.query.get(userid)

class User(flask_login.UserMixin, db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    status  = db.Column(db.String(1024), default="")
    name    = db.Column(db.String(64))
    email   = db.Column(db.String(128))
    age     = db.Column(db.Integer)
    pwd     = db.Column(db.String(64))

    posts   = db.relationship("Post", backref='user', lazy='dynamic')

    def get_id(self):
        return self.user_id

    def update_profile(self, status, name, email, age):
        self.status = status
        self.name = name
        self.email = email.lower()
        self.age = age

        db.session.commit()

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.String(512))
    date    = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    author  = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def get_human_date(self):
        return "{}/{}/{}".format(self.date.day, self.date.month, self.date.year)





