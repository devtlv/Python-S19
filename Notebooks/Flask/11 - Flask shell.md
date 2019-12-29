# Flask shell

Flask provide a shell that can be runned by executing `$ flask shell`, if nothing is configured, it's just a python shell.<br>

<a href="http://flask.pocoo.org/docs/1.0/shell/">Documentation</a>

# Flask shell context


## A context is some variables that are pre imported in the shell

Those variables are called a context, they can be defined in a function which will be decorated by the `app.shell_context_processor` decorator.
It should be declared in your `FLASK_APP` file. <br>
This function should return a dictionnary of keyword arguments, which look like this


```python
from app import app, db
from app.models import MyModel

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'MyModel': MyModel}
```

# Playing with the shell

Shell can be really useful to test things, add/delete models to the database, generate objects etc..
