#!/usr/local/bin/python3
#
# models.py
# pyblog
#

from pyblog import db, login_mgr
import flask_login

@login_mgr.user_loader
def load_user(userid):
    userid = int(userid)
    return User.query.get(userid)

class User(flask_login.UserMixin, db.Model):

    user_id = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64))
    age     = db.Column(db.Integer)
    pwd     = db.Column(db.String(64))

    def get_id(self):
        return self.user_id



