# PostgreSQL

- Open source
- SQL
- Scalable
- Compatible with Sql-Alchemy

More on https://www.postgresql.org/about

### Installation
For MAC OSX: https://postgresapp.com/  
For Windows: https://www.postgresql.org/download/
For linux: See your distribution documentation, you may need to start it with `systemctl`

> Follow the documentation !

### Create a database
To start the postgres CLI, type `psql` in the shell. Then you can type all the postgres commands, for example: `CREATE DATABASE <database_name>`.   

### Python requirements
To use PostgreSQL with Flask and Flask-SQLAlchemy, you need another module (that is used by flask-sqlalchemy, you won't need to use it) called `psycopg2`, install it with pip.  

### Differences between SQLite and PostgreSQL
SQLite is a local file, while PostgreSQL is a remote database (it sits on a server), we need to change a few things in the code.  
First, the config `app.config['SQLALCHEMY_DATABASE_URI']` needs to be changed, because currently it is pointing to a local file, and Postgres database is on a server. The value of this config should be the URL of the Postgres database.  
You can put this directly in your code:
```
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://url/to/database"
```
You can also define it as an environnement variable (for more flexibility), to do so, type this in the terminal:  
`> export DATABASE_URL="postgresql://url/to/database"`  
And use `os` module to retrieve it in your code:  
```
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
```

> Be careful, if you don't define this environnement variable in the terminal before using it, you will have an error.   

### Lookup
To look at the content of the database, enter the `psql` CLI.  
1. To connect to the database, type `\c database_name`  
2. To print all the tables , type `\dt`  
3. To lookup a specific table, type `\d table_name`

### New things

PostgreSQL brings a few new features, like the `JSON` column, to use it you need to import it specifically because this column is not supported by every database.  

```
from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'results'

    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    meta = db.Column(JSON)
```





