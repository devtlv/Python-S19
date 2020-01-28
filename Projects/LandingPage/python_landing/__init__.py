import flask, flask_sqlalchemy, flask_migrate, flask_login
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)

# Db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

# Login config
login_mgr = flask_login.LoginManager(app)

from python_landing import routes, models
