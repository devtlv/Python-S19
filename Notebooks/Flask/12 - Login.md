# Login

***
### Login module

`flask-login` is the module that wraps all the logins functions, install it with pip

This module provide a login manager, `flask_login.LoginManager` class, to create an object:


```python
import flask
import flask_login

app = flask.Flask()
# ...

login_mngr = flask_login.LoginManager(app)

# ...
```

This login manager need us to modify a little our `User` model, because it needs some special attributes, listed below:<br>

-    `is_authenticated`: a property that is True if the user has valid credentials or False otherwise.
-    `is_active`: a property that is True if the user's account is active or False otherwise.
-    `get_id()`: a method that returns a unique identifier for the user as a string.
-   `is_anonymous`: a property that is False for regular users, and True for a special, anonymous user.

> Anonymous user is a user that is not logged in.



We can implement those attributes, manually, but we can also change our user model to inherit from `flask_login.UserMixin`, which is appropriated for almost every user class.


```python
from app import db
import flask_login

# ...
class User(flask_login.UserMixin, db.Model):
    #...
```

***
## User Loader Function

flask_login keep trace of logged in user with user id, but he doesn't know anything about the database, we need to help him to retrieve a user from an id.<br>
We do this with a function decorated by `LoginManager.user_loader` decorator.


```python
from app import login_mngr, models
#...

@login_mngr.user_load
def load_user(userid):
    userid = int(userid)
    return models.User.query.get(userid)
```

*** 
## Retrieve the current user
`flask_login.current_user` allows us to retrieve the current user logged in.

***
## Loading a user in 

`flask_login` implement a `login_user` method that can be used to log a user in, this function doesn't make any password check. 
> This view is assuming you already created a login form that contains *username*, *password* and *remember_me* fields, but you can adapt it to yours.


```python
# ...
import flask_login
from app import models

# ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated: # Check if the user is not already logged in 
        return flask.redirect(url_for('index'))
    
    form = forms.LoginForm() # Load the form
    
    if form.validate_on_submit(): 
        # Retrieve the user with the username
        user = models.User.query.filter_by(username=form.username.data).first()
        
        # Check if it exist and if the password is the right password
        if user is None or not user.password == form.password.data:
            flask.flash('Invalid username or password')
            return flask.redirect(url_for('login'))
        
        # Log the user in
        flask_login.login_user(user, remember=form.remember_me.data)
        return flask.redirect(url_for('index'))
    
    return flask.render_template('login.html', title='Sign In', form=form) # Render the form
```

***
## Logging user out



```python
# ...
import flask_login

# ...

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect(url_for('index'))
```

***
## Using flask_login methods in templates
Updating a button on the top:
    <div>
        <a href="{{ url_for('index') }}">Home</a>
        {% if current_user.is_anonymous %}
        <a href="{{ url_for('signin') }}">Sign In</a>
        {% else %}
        <a href="{{ url_for('logout') }}">Logout</a>
        {% endif %}
    </div>
***
## Requiring Users To Login
Flask-Login provides a very useful feature that forces users to log in before they can view certain pages of the application.<br>
To use that feature, flask_login needs to know which view handle logins, in our case, it's `login`, we need to configure this in the `__init__.py` of the app.


```python
# ...
login_mngr = LoginManager(app)
login_mngr.login_view = 'login'
```

Then, you can use the `flask_login.login_required` decorator to protect a view from anonymous users


```python
import flask_login 

@app.route('/secret')
@flask_login.login_required
def secret():
    # ...
```

***
## Showing The Logged In User in Templates
`flask_login.current_user` can be accessed from templates

{% extends "base.html" %}

{% block content %}
    <h1>Hi, {{ current_user.username }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}