#!/usr/local/bin/python3
#
# forms.py
# pyblog
#

import flask_wtf
import wtforms

class SignupForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name")
    age  = wtforms.IntegerField("Age")
    pwd  = wtforms.PasswordField("Password")

    submit = wtforms.SubmitField("Signup")




