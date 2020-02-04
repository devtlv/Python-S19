import flask_login
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from python_landing import db, app

topic_to_tag = db.Table('topic_to_tag',
                        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), 
                                  primary_key=True),
                        db.Column('topic_id', db.Integer, db.ForeignKey('topic.id'),
                                  primary_key=True),
                )

class User(db.Model, flask_login.UserMixin):
    id          = db.Column(db.Integer, primary_key=True)
    username    = db.Column(db.String(64))
    pwd         = db.Column(db.String(64))
    email       = db.Column(db.String(128))

    topics      = db.relationship('Topic', backref='author')
    messages    = db.relationship('Message', backref='author')

    def change_pwd(self, pwd):
        pwd_hash = generate_password_hash(pwd)
        self.pwd = pwd_hash
        db.session.commit()

    def check_pwd(self, pwd):
        return check_password_hash(pwd)

    def get_recovery_pwd_token(self, expires=600):
        exp_date = datetime.datetime.now() + datetime.timedelta(0, expires*60)
        payload = {
            'id': self.id,
            'exp': exp_date
        }
        secret_key = app.config['SECRET_KEY']

        token = jwt.encode(payload, secret_key, algorithm="HS256")

        return token.decode('utf-8')

    @classmethod
    def get_user_from_token(cls, token):
        secret_key = app.config['SECRET_KEY']
        payload = jwt.decode(token, secret_key, algorithm="HS256")
        if datetime.datetime.now() > payload['exp']:
            return False

        user_id = payload['id']

        return User.query.get(user_id)




class Topic(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(128))
    body    = db.Column(db.String())
    time    = db.Column(db.DateTime(), default=datetime.datetime.now())

    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    messages = db.relationship('Message', backref='topic')
    tags     = db.relationship('Tag',
                               secondary=topic_to_tag,
                               back_populates='topics'
                              )

class Message(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    body    = db.Column(db.String())
    time    = db.Column(db.DateTime(), default=datetime.datetime.now())

    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

class Tag(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    topics = db.relationship('Topic',
                             secondary=topic_to_tag,
                             back_populates='tags'
                            )
