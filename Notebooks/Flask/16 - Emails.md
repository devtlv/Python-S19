# Send emails with flask-mail
### Before anything: install flask-mail
$ pip install flask-mail
### First
You need to set a bunch of config in your app  



```python
app.config['MAIL_SERVER']     = 'smtp.gmail.com'
app.config['MAIL_PORT']       = 587
app.config['MAIL_USE_TLS']    = True
app.config['MAIL_USE_SSL']    = False
app.config['MAIL_USERNAME']   = 'awetandtesfit@gmail.com'
app.config['MAIL_PASSWORD']   = 'Micheal79'
```

> You need to allow less secure apps on your google account for this to work, to do so, follow this link:
> https://myaccount.google.com/lesssecureapps


# Create an email manager with flask_mail

flask_mail provide a `Mail` class that allow you to send mails.<br>

<small>In the __init__.py</small>


```python
# ...
import flask_mail

# ...

app = flask.Flask(__name__)
# define the mail object
mail = flask_mail.Mail(app)

# ...
```

# Send an email

To send an email, you first need to create the message object


```python
msg = flask_mail.Message('subject', 
                         sender='mymail@gmail.com', 
                         recipients=['receiver1@example.com', 
                                     'receiver2@example.com'])
```

And then add some content to the mail, you can add text content or HTML content


```python
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
```

To send the message, you need to use the `send` function of the mail manager


```python
mail.send(msg)
```

We can add every mailing functions in an `mailing.py` file.


```python
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)
    
```

> You can render a template and send it by email

# Add a "lost password" function

### First: let's create a function to send the email
We could create a function like this:


```python
def send_password_reset_email(user):
    send_email('Password reset',
               sender="mymail@gmail.com",
               recipients=[user.email],
               text_body=flask.render_template('email/reset_password.txt', user=user),
               html_body=flask.render_template('email/reset_password.html', user=user)
```

But the problem is, we can't identify if the person that is requesting is actually the user, we need to use a token. A token is a little encoded string, that will only belong to the user.<Br>
<a href="https://pyjwt.readthedocs.io/en/latest/">`pyJWT`</a> is a library that provide some functions to deal with tokens, with this library, we can encode some data with a key.
> JWT stands for <a href="https://en.wikipedia.org/wiki/JSON_Web_Token">Json Web Token</a>
    
The key we will use to encode the payload will be our secret key.<br>
We need the `jwt.encode` function to create an encoded token.<br>
Let's implement a function that create a token in our user model:<br>
<br>
<small>In User model:</small>


```python
import time
import jwt
#class User(...):
    #...
    def get_reset_password_token(self, expires_in=600):
        timeout = time.time() + expires_in
        payload = {
            'reset_password': self.id,
            'exp': timeout
        }
        
        # Get the secret key from config
        secret_key = app.config['SECRET_KEY']
        
        # Create the token
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        
        # Turn it to string
        s_token = token.decode('utf-8')
        
        return s_token

```

We can now update our `send_password_reset_email` function


```python
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('Password reset',
               sender="mymail@gmail.com",
               recipients=[user.email],
               text_body=flask.render_template('email/reset_password.txt', user=user, token=token),
               html_body=flask.render_template('email/reset_password.html', user=user, token=token))
```

This token is supposed to allow us to identify the user that its's linked to.<Br>
We also need to add a function to verify this token.<br>
<br>
<small>In the User model:</small>



```python
import time
import jwt

#class User(...):
    #...
    def get_reset_password_token(self, expires_in=600):
        timeout = time.time() + expires_in
        payload = {
            'reset_password': self.id,
            'exp': timeout
        }
        
        # Get the secret key from config
        secret_key = app.config['SECRET_KEY']
        
        # Create the token
        token = jwt.encode(payload)
        
        # Turn it to string
        s_token = token.decode('utf-8')
        
        return s_token

    def verify_reset_password_token(self, token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
```

### Now, let's create the templates for the function

Let's create the two templates for text and html body
<br>
<small>reset_password.txt:</small>
Dear {{ user.username }},

To reset your password click on the following link:

{{ url_for('reset_password') }}

If you have not requested a password reset simply ignore this message.
And the html template
<br>
<small>reset_password.html:</small>
<p>Dear {{ user.username }},</p>
<p>
    To reset your password
    <a href="{{ url_for('reset_password') }}">
        click here
    </a>.
</p>
<p>Alternatively, you can paste the following link in your browser's address bar:</p>
<p>{{ url_for('reset_password', token=token, _external=True) }}</p>
<p>If you have not requested a password reset simply ignore this message.</p>
### Step 2: let's create a form to request the mail

This page requires a form, so we need a form, a template and a route:<br>
<br>
<small>Form:</small>


```python
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
```

<small>Template:</small>
{% extends "base.html" %}

{% block content %}
    <h1>Reset Password</h1>
    <form action="" method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.email.label }}<br>
            {{ form.email(size=64) }}<br>
            {% for error in form.email.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}
<small>Route:</small>


```python
from app import forms, mailing

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = forms.ResetPasswordRequestForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user:
            mailing.send_password_reset_email(user)
            
        flash('An email has been sent')  
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form)
```

### Step 3: When the user has clicked on the mail, he needs to get to a Reset password form

Form:


```python
class ResetPasswordForm(FlaskForm):
    password = wtforms.PasswordField('Password', validators=[DataRequired()])
    confirm  = wtforms.PasswordField('Confirm Password', validators=[validators.DataRequired(), validators.EqualTo('password')])
    submit = wtforms.SubmitField('Request Password Reset')
```

Template:
{% extends "base.html" %}

{% block content %}
    <h1>Reset Your Password</h1>
    <form action="" method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.password2.label }}<br>
            {{ form.password2(size=32) }}<br>
            {% for error in form.password2.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}
# That's it !

---

> You can send your mail as a thread if it slows down your application


```python

```
