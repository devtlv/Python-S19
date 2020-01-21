#!/usr/local/bin/python3
#
# forms.py
# pyblog
#

import flask_wtf
import wtforms
import wtforms.validators as vld


class EqualToCI:

    def __init__(self, target_field, message=""):
        self.target_field = target_field
        self.message      = message

    def __call__(self, form, field):
        if field.data.lower() != self.target_field.data.lower():
            raise wtforms.ValidationError(self.message)

class SignupForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name")
    age  = wtforms.IntegerField("Age")
    pwd  = wtforms.PasswordField("Password")
    pwd_confirm = wtforms.PasswordField("Confirm password", 
                                        validators=[EqualToCI('pwd', message="PLEASE PUT THE SAME PASSWORD IN THE TWO FIELDS")])
    submit = wtforms.SubmitField("Signup")

class SigninForm(flask_wtf.FlaskForm):
    name         = wtforms.StringField("Name")
    pwd          = wtforms.PasswordField("Password")
    remember_me  = wtforms.BooleanField("Remember me")
    submit       = wtforms.SubmitField("Sign in")







