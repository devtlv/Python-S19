# User Profile Page

## Receiving arguments in URL
We can receive arguments in url by surrounding them with `<` and `>`. Those arguments will be sent in the function `**kwargs`.<br>
For example:


```python
@app.route('/users/<user_id>')
def show_user(user_id): # user_id will be filled by the value passed in the url
    models.User.get(user_id) 
```

Let's create a simulation of a profile page.<br>
__Template:__
{% extends "base.html" %}

{% block content %}
    <h1>User: {{ user.username }}</h1>
    <hr>
    {% for post in posts %}
    <p>
    {{ post.author.username }} says: <b>{{ post.body }}</b>
    </p>
    {% endfor %}
{% endblock %}
__View:__


```python
@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
```

***
## Adding a *Last seen* option to the model
We can add a *last seen* option in the model


```python
from datetime import datetime
class User(UserMixin, db.Model):
    # ...
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    # ...
```


But we need to update it, we can do it in the login view function, in routes.py.


```python
from datetime import datetime

def login_view():
    # ... 
    user = User(#...)
    user.last_seen = datetime.utcnow
```

Then, updating the template should be easy
#...

<h1>{{ user.username }}</h1>
<p>Last seen on: {{ user.last_seen }}</p>
#...
***
## Adding a *Status*

We can add a status attribute, first add it to the model


```python
from datetime import datetime
class User(UserMixin, db.Model):
    # ...
    status = db.Column(db.String(140), default="Hello World !")
    # ...
```

Then render it on the template

<h1>User: {{ user.username }}</h1>
<p>{{ user.about_me }}</p>
***
## Add a profile editor 

We can add a page for the user to edit his profile. To modify status, password or email. This page needs user input, so it should be a form. For now, let's only add a field to modify the status. <br>
We can use a different type of field for this, the `TextAreaField`, which will display a box to input the data.
import wtforms
from wtforms import validators

class ProfileEditorForm(wtforms.FlaskForm):
    about_me = wtforms.TextAreaField('About me')
    submit = wtforms.SubmitField('Submit')
The template needs to be modified a little, `TextAreaField` needs two parameters: a number of rows and a number of columns.
<p>
    {{ form.about_me.label }}<br>
    {{ form.about_me(cols=50, rows=4) }}<br>
</p>
We also need a back end function to handle this. In *routes.py*:


```python
from app import forms

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = forms.ProfileEditorForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        return flask.redirect(url_for('edit_profile'))
    return flask.render_template('edit_profile.html', title='Edit Profile',
                           form=form)
```

## Pre-fill the fields in the form

In fact, `form.validate_on_submit()` return false if the form contains errors OR if the request sent by the user wasn't POST, PUT, PATCH or DELETE.<br>
When the form is being requested, a GET request is sent, we need to use this GET request to fill the fields in the post. The GET request the "*initialization*" of the form<br>
We can check the type of the request by using `request.method`.<br>
<br>
When the form is requested, we want to assign value to the `about_me` field.



```python
from app import forms

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = forms.ProfileEditorForm()
    
    if form.validate_on_submit():
        
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        
        db.session.commit()
        
        return flask.redirect(url_for('edit_profile'))
    
    elif request.method == 'GET':                  # if the request method is GET
        form.about_me.data = current_user.about_me   # assign a value to the about_me form
        
    return flask.render_template('edit_profile.html', title='Edit Profile',
                           form=form)
```
