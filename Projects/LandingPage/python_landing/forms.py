import flask_wtf
from flask_wtf import FlaskForm
import wtforms as wtf
from wtforms import *
from wtforms.validators import *


class PwdModifForm(flask_wtf.FlaskForm):

    new_pwd  = wtf.PasswordField('New password')

    submit   = wtf.SubmitField("Change your password")

class LostPwdForm(flask_wtf.FlaskForm):

    email = wtf.StringField('Email')

    submit = wtf.SubmitField('Send a password recovery email')

class LoginForm(FlaskForm):
    email       = StringField("Email")
    pwd         = PasswordField("Password")
    remember_me = BooleanField("remember_me")
    submit = SubmitField("Login")

class SignupForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    pwd   = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Signup")
