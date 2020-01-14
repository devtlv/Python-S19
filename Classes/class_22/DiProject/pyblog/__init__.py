import flask
import os
import flask_sqlalchemy
import flask_migrate

app = flask.Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__)) # Try to avoid hardcoding paths, use os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
# This line is adding sqlite:/// with the path of your database

db      = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from pyblog import routes, models
