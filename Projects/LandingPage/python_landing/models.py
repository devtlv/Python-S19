import flask_login
import datetime

from python_landing import db

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
