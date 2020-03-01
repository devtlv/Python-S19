import flask
import os
import flask_sqlalchemy
import flask_migrate
import flask_login


app = flask.Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SECRET_KEY'] = 'ILOVECHOCOLATE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

login_mgr = flask_login.LoginManager(app)

from app import routes, models



