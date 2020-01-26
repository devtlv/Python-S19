from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    customer_name = StringField("customer_name")
    customer_password = PasswordField("customer_password")
    remember_me = BooleanField("remember_me")
    submit = SubmitField("Login")

class SignupForm(FlaskForm):
    customer_name = StringField("customer_name",validators=[DataRequired()])
    customer_password = PasswordField("customer_password",validators=[DataRequired()])
    submit = SubmitField("Signup")