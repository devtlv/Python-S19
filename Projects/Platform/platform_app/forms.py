import flask_wtf
import wtforms as wtf
import wtforms.validators as vld

class SigninForm(flask_wtf.FlaskForm):
    mail = wtf.StringField('Email', )
    pwd  = wtf.PasswordField('Password', )
    submit = wtf.SubmitField('Sign in')

class SignupForm(flask_wtf.FlaskForm):
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


