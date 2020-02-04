import flask_login

from platform_app import db, login_mgr

@login_mgr.user_loader
def load_user(id):
    return User.query.get(id)

class User(flask_login.UserMixin, db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64))
    role    = db.Column(db.String(64))
    mail    = db.Column(db.String(128))
    pwd     = db.Column(db.String(64))

