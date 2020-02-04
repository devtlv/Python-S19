from platform_app import db

class User(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(64))
    role    = db.Column(db.String(64))
    mail    = db.Column(db.String(128))
    pwd     = db.Column(db.String(64))
