#!/usr/local/bin/python3
#
# forms.py
# pyblog
#

import flask_wtf
import wtforms
import wtforms.validators as vld


def contains_eyal(form, field):
    if 'eyal' not in field.data:
        raise wtforms.ValidationError('Your field needs to contain EYAL')

class SignupForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name", validators=[contains_eyal])
    age  = wtforms.IntegerField("Age")
    pwd  = wtforms.PasswordField("Password")
    pwd_confirm = wtforms.PasswordField("Confirm password", 
                                        validators=[vld.EqualTo('pwd', message="PLEASE PUT THE SAME PASSWORD IN THE TWO FIELDS")])
    submit = wtforms.SubmitField("Signup")










