# Structure of the project

## Once you have big projects, you need to organize your folders
Let's create a new project called `blogs`

# 1) The `app` folder

This folder will contain every file that is part of the application: the models, the views, the templates etc...<br>
<br>
**** 
### `__init__.py`
This folder is a python package, we can add a `__init__.py` file that will be ran when the package is imported.<br>
In this `__init__.py` file, we're going to define every big variable, like the app and the database. For now, let's only define the app.
<br>
<br>


```python
import flask

app = flask.Flask(__name__) # Remember: __name__ is the name of the file where the code is written
```

***
### `templates`

This folder contains every templates (html files) that the app need, let's add `index.html`
{% extends "base.html" %}

{% block content %}
    <h1>Posts:</h1>
    {% for post in posts %}
    <div><p>{{ post.author }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}
 


***


### `routes.py`
This file will contain every view of the app, let's create a real quick one.
<br>


```python
# First, we are in a different file, so we need to import the app
import flask
from app import app    # app.app is package_name.variable_name

@app.route("/")
def index():
    posts = [
        {"author":"Eyal", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]
    return flask.render_template(posts=posts)
```

## Now in the project folder, let's add the main file
Called `blogs.py`.<br>
In this file, we want to import the app and then run it


```python
from app import app

if __name__ == "__main__":         # Protect this code to be ran if he is imported
    app.run(port=5000, debug=True)
```

***

## For now, here is how the project looks like:


blogs/
- app/
-- __init__.py
-- routes
-- templates/
--- index.html
- blogs.py
# Let's run it

We are no longer running the project inside pycharm, now we will run it in terminal.<br>
In terminal, you need to activate the virtualenv, and then you can launch flask commands by typing `$ flask <command>`.<br>
The first command that we want to use is `$ flask run`, this command will launch the main app of the project. But to make this work, we need to tell flask which file is the main one. This is done by typing:
> Unix: `$ export FLASK_APP=<your_main_file>`<br>
> Windows: `$ set FLASK_APP=<your_main_file>`
<br>

And now we can launch `$ flask run`

***
> Get back after reading theory on web forms
***

# Add a `forms.py` file 
This file should contain every form of the app.
