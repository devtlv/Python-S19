import flask, flask_sqlalchemy, flask_migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from platform_app import routes, models
