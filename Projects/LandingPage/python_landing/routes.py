from python_landing import app, models, mailing, forms
import requests
import flask
import flask_login
from python_landing.forms import *

@app.route('/')
def homepage():
    return flask.render_template('homepage.jin')

@app.route('/news')
def news():
    api_key = "e9ea763d28384a2ea98fea09dbaf8720"
    url = "https://newsapi.org/v2/everything?q=python&apiKey={}".format(api_key)
    r = requests.get(url)
    content = r.json()

    return flask.render_template('news.jin', news=content['articles'])

@app.route('/forum')
def forum():
    topics = models.Topic.query.all()

    return flask.render_template('forum.jin', topics=topics)

@app.route('/forum/<int:topic_id>')
def topic_page(topic_id):
    topic = models.Topic.query.get(topic_id)

    return flask.render_template('topic_page.jin', topic=topic)

@app.errorhandler(404)
def error_404(err):
    print(err)
    return flask.render_template("404_error.jin")

@app.route('/mail-test')
def send_mail():
    mailing.send_mail(
        subject="Hello world",
        recipients=['me@gmail.com'],
        body="Hello from my flask app",
        html="<h1>Hello from my flask app</h1>"
    )

    return "Done."

# Logins
@app.route('/change-password/<token>', methods=('GET', 'POST'))
def change_pwd(token):
    form = forms.PwdModifForm()
    if flask.request.method == 'POST':
        if form.validate_on_submit():
            user = models.User.get_user_from_token(token)
            if user is None:
                flask.flash("User doesn't exist")
            elif user is False:
                flask.flash("Token is expired")
            else:
                user.change_pwd(form.new_pwd.data)

    return flask.render_template('change_pwd.jin', 
                                form=form)

@app.route('/lost-password', methods=('GET', 'POST'))
def lost_pwd():
    form = forms.LostPwdForm()
    if flask.request.method == 'POST':
        if form.validate_on_submit():
            mail = form.email.data
            user = models.User.query.filter_by(mail=mail).first()
            if not user:
                return flask.redirect('homepage')

            change_pwd_url = flask.url_for('change_pwd', token=user.get_recovery_pwd_token())
            mailing.send_mail(
                subject="Password recovery",
                recipients=[mail],
                text="Click below to change your password ! {}".format(),
                html=""
            )
            flask.flash("An email has been sent to",mail)
            return flask.redirect('homepage')

    return flask.render_template('lost_pwd.jin', form=form)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()  # Load signup the form

    if form.validate_on_submit():

        user = models.User(username=form.username.data,
                            status="active")

        user.change_pwd(form.pwd.data)

        db.session.add(user)
        db.session.commit()

        flask_login.login_user(user)

        return flask.redirect(url_for('homepage'))

    return flask.render_template('sign_up.jin', title='Sign UP', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(url_for('homepage'))

    form = forms.LoginForm()  # Load the form

    if form.validate_on_submit():
        user = models.User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_pwd(form.pwd.data):
            flask.flash('Invalid user Name or password')
            return flask.redirect(url_for('login'))

        # Log the user in
        flask_login.login_user(user, remember=form.remember_me.data)
        return flask.redirect(url_for('homepage'))

    return flask.render_template('sign_in.jin', title='Sign In', form=form)  # Render the form

@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return redirect(url_for('homepage'))








