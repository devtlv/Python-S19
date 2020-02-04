#!/usr/local/bin/python3

from platform_app import app, db, models

def create_superuser():
    user = models.User()
    user.name  = "Super User"
    user.email = "eyal@chocron.eu"
    user.pwd   = "chocolate"
    user.role  = "admin"
    db.session.add(user)
    db.session.commit()

