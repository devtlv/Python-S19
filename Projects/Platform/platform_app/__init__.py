import flask, flask_sqlalchemy, flask_migrate, flask_login
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'aweusdhbjcaiuweyurgdyfdiq3uye28q7wyexne982qzun3e2q##$39x8un9'

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'app.db')

login_mgr = flask_login.LoginManager(app)

from platform_app import routes, models
