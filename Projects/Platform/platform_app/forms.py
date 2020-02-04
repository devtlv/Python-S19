import flask_wtforms as flask_wtf
import wtforms as wtf
import wtf.validators as vld

class SigninForm():
    mail = wtf.StringField('Email', validators=[vld.Email()])
    pwd  = wtf.PasswordField('Password', validators=[vld.DataRequired()])
    submit = wtf.SubmitField('Sign in')

class SignupForm():
    name = wtf.StringField("Name", validators=[vld.DataRequired()])
    role = wtf.SelectField("Role",
                           choices=[
                               ('student', 'Student'),
                               ('teacher','Teacher'),
                               ('demo','Demo')
                            ])
    mail = wtf.StringField('Email', validators=[vld.Email()])
    pwd  = wtf.PasswordField('Password', validators=[vld.DataRequired()])
    submit = wtf.SubmitField('Sign up')


