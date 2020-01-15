# Databases & Models

## SQL or NoSQL ? 
There are great choices for databases in Python, and most of them with flask integration.<br>
They can be separated into two big groups: SQL and NoSQL.<br>
<br>
Basically, __SQL__ is a better match for application with structured data (list of users, blogs..) while __NoSQL__ tend to be better for less defined structure.

***
## Databases 

A lot of databases exist, every database has his own pros and cons, some are better for really big databases, some other for little sites..<br>
`MySQL` is relatively easy to use and to configure since it only needs a single file to store a db.

***
## ORM
Using database queries is low-level work, and some higher level extensions are available in Python to make our life easier.<br>
__ORM__, or *Object Relational Mapping* is a technique that alows us to convert data from database to objects.<br><br>

__ORMs__ will create a virtual database as an object in python, thus the data will also be represented as objects.<br>
<br>

We are going to use *SQLAlchemy* ORM, which can support a long list of database engines, like MySQL, PostgreSQL and SQLite. <br>
<Br>
The same code will work no matter which database engine you're using, and __this is very powerful.__
<br>
<br>
A wrapper for SQLAlchemy exist for flask, it's called `flask-sqlalchemy`. To install it, use pip. 



***
## Migration
Relational database (SQL) needs to be structured, thus we need to update the database everytime we change something in its structure.
> *Changing his structure doesn't mean adding some data, but adding/deleting a table.*

Updating database structure is called *migration*, a good migration framework in python is <a href="https://bitbucket.org/zzzeek/alembic">Alembic</a>, the flask wrapper is called `flask-migrate`.

> *Reminder: flask_sqlalchemy is the database manager and flask_migrate is the migration manager*

***
# Code

## Configuring Flask-SQLAlchemy
We need to add some configuration to our app to define the implementation of `flask_sqlalchemy`.<br><br>

The main configuration is the database uri (the location of the database). <br>
This is defined by `app.config['SQLALCHEMY_DATABASE_URI']`.<br>
*In the `__init__.py`:*


```python
import os 
basedir = os.path.abspath(os.path.dirname(__file__)) # Try to avoid hardcoding paths, use os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
# This line is adding sqlite:/// with the path of your database
```

***
## Create a database object 

A database is a virtual object, it can be created with the class `flask_sqlalchemy.SQLAlchemy`.<br>
Migration is also a virtual object, that is part of the `flask_migrate.Migrate` class.<br>
*In the `__init__.py`:*


```python
import flask
import flask_sqlalchemy
import flask_migrate
import os 

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')

db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import routes
```

***
## Database models

In ORM, tables are called models, a model represent a class of data. <br>
To visualize your database, you can use the <a href="https://ondras.zarovi.cz/sql/demo/">SQL Designer</a> tool.<br>
Every model should inherit from the `flask_sqlalchemy.SQLAlchemy().Model` class, which can be accessed from your object.<br>
>`class MyModel(db.Model)`<br>

<br>
All the models should be in a `models.py` file, in the app folder
<br> <br>
You can represent a model as a table, every row is a new object, and every column is an attribute.<br>
To add attributes to the model, you need to add columns, represented by a <a href="https://docs.sqlalchemy.org/en/13/core/metadata.html#sqlalchemy.schema.Column">Column</a> object. <br>
The only required argument is the type of column<br><br>
For example:<br>



```python
from app import db

class MyModel(db.Model):
    
    field1 = db.Column(db.String(64))
    field2 = db.Column(db.Integer)

```

### Adding arguments to the fields
-  Adding a primary key: A primary key is a field that is filled automatically, it's a unique key that allows us to identify the object. It's an id.<br>
`id = db.Column(db.Integer, primary_key=True)`
-  Adding an index: We can add an argument that index the column, which allow us to sort our data by this column values.<br>
`username = db.Column(db.String(64), index=True)`<br>
-  Adding a default value: We can add a value in case this field is not filled at the creation, with the `default` argument.<br>
`time = db.Column(db.DateTime, default=datetime.now)`<br>

> You can add a `__repr__` function to your model to make the prints more clear

***
## Manage the real database 

Even if the database is an object in flask, it has to be a real file behind the scenes, flask commands allow us to manage it.

### `flask db` 
`$ flask db` is a flask db manager, there is a few important commands to know.
-  `$ flask db init`, the first command that you need to run, it creates the database, you need to run it when it's the first time you use this database.
-  `$ flask db migrate`, every time you make changes in the database structure, you need to migrate it, it updates the database structure but it doesn't apply those updates
-  `$ flask db upgrade`, this time, flask update your changes and change the database structure

***
## Add new objects to the database
Once you have your Model class, you can create some objects very simply.


```python
model1 = MyModel(field1="HelloWorld", field2=1000)
```

But this is just an object, you need to add it to the database.
> Reminder, your database is represented by an object, here it's called `db`

You can use some methods of the db object to add it to your database.


```python
db.session.add(model1)
db.session.commit()
```

`db.session.add` is just adding an object to the database object, but the real database will only be modified when `db.session.commit` is called.<br>
Basically, `db.session.commit` is updating the real database with the virtual object

If something went wrong, you can always use


```python
db.session.rollback()
```

You can also delete some objects from the database.


```python
db.delete(obj)
```

***
## Retrieve objects from the database
Database objects have a `query` attribute that allow us to *query* the database (ask the database for some data).<br>

### Retrieve every objects from a certain class
`MyModel.query.all()` returns a list with every object of the Model `MyModel`

### Retrieve a specific object 
You can retrieve a list of objects that fit a condition with `MyModel.query.filter_by(filter)`, for example `User.query.filter_by(username="Eyal")` will retrieve a list of all users that have `Eyal` as username<br>
To select one from this list, a lot of selectors are available <a href="">here</a>, like `first()` or `first_or_404()`

> A primary key is a unique "id" for every object, it can be defined in each column definition by the `primary_key=True` parameter.

# Conclusion

-  `flask_sqlalchemy` and `flask_migrate` are both required to deal with databases, one for the database and the other for the structure.
-  `SQLALCHEMY_DATABASE_URI` is required to implement the database in the app
-  Database is built with `SQLAlchemy` class and migration with `Migrate` class.
-  Models have to be classes that inherit from `db.Model`.
-  Models should contain columns that are instances of `db.Column`
-  To create a new object in the database, first create python object (an instance of the model), and then pass it through `db.session.add` to stage it, and run `db.session.commit()` to add all the staged objects to the real database.
