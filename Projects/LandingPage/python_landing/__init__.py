import flask, flask_sqlalchemy, flask_migrate, flask_login, flask_mail
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'ewisfudzcxbhjnawsudfbcaszdhufcas'

# Db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

# Login config
login_mgr = flask_login.LoginManager(app)

# Mail config
app.config['MAIL_SERVER']     = 'smtp.gmail.com'
app.config['MAIL_PORT']       = 587
app.config['MAIL_USE_TLS']    = True
app.config['MAIL_USE_SSL']    = False
app.config['MAIL_USERNAME']   = 'foo@bar.com'
app.config['MAIL_PASSWORD']   = 'yourpassword'

mail_mgr = flask_mail.Mail(app)

from python_landing import routes, models
