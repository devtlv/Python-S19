import flask, flask_login
import requests
from urllib.parse import urljoin
import markdown

from platform_app import app, forms, models, route_filters, db

@app.route("/")
def homepage():
    return flask.render_template('homepage.jin')

@app.route('/sign-in', methods=('GET', 'POST'))
def signin():
    form = forms.SigninForm()
    if form.validate_on_submit():
        email = form.mail.data
        user = models.User.query.filter_by(mail=email).first()

        if user and user.pwd == form.pwd.data:
            flask_login.login_user(user)
            return flask.redirect(flask.url_for('homepage'))
        else:
            print("Wrong password")
            print(user)
    else:
        print(form.errors)

    return flask.render_template('signin.jin', form=form)

@app.route('/sign-out')
def signout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('homepage'))

@app.route("/users/create", methods=("GET", "POST"))
@route_filters.role_required('admin', 'teacher')
def create_user():
    form = forms.SignupForm()
    if form.validate_on_submit():
        user = models.User()
        user.name = form.name.data
        user.mail = form.mail.data
        user.role = form.role.data
        user.pwd  = form.pwd.data

        db.session.add(user)
        db.session.commit()

        flask.flash("{} has been created".format(user.name))

        return flask.redirect(flask.url_for('homepage'))

    return flask.render_template('signup.jin', form=form)

@app.route("/display-course/<path:url>")
def display_course(url):
    base_url = "https://raw.githubusercontent.com"

    # Build url
    endpoint = urljoin(base_url, url)

    # Download content
    r = requests.get(endpoint)
    raw_content = r.text

    md = markdown.Markdown()
    html_content = md.convert(raw_content)

    # Display content (through a template)
    return flask.render_template("display_course.jin",
                                 html_content=html_content)




