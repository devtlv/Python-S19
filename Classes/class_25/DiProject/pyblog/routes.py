from pyblog import app, db
from pyblog import models, forms
import flask
import flask_login

@app.route('/')
def homepage():
    daily_quote = "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"
    return flask.render_template("homepage.jin", daily_quote=daily_quote)

@app.route("/about-us")
def about():
    return flask.render_template('about.jin')

@app.route("/users")
def users_list():
    users = models.User.query.all()
    return flask.render_template('users_list.jin', users=users)

@app.route('/users/<int:user_id>') 
def userpage(user_id):
    user = models.User.query.get(user_id)
    if not user:
        flask.flash("User doesn't exist.")
        return flask.redirect(flask.url_for('homepage'))
    return flask.render_template('user_page.jin', user=user)

@app.route("/sign-in", methods=('GET', 'POST'))
def signin():
    # Handle Already signed in user

    signin_form = forms.SigninForm()

    if flask.request.method == 'POST':
        # Do the whole post-form process
        if signin_form.validate_on_submit():
            # Retrieve info passed in form
            name = signin_form.name.data
            pwd  = signin_form.pwd.data
            remember = signin_form.remember_me.data

            userlist = list(models.User.query.filter_by(name=name))
            if not userlist:
                flask.flash("User {} doesn't exist".format(name))
                return flask.render_template("signin.jin", form=signin_form)

            user = userlist[0]
            if user.pwd == pwd:
                flask_login.login_user(user, remember=remember)
                flask.flash(user.name + " logged in !")
                return flask.redirect(flask.url_for('homepage'))
            else:
                flask.flash("Invalid credentials")

    return flask.render_template("signin.jin", form=signin_form)


@app.route("/sign-up", methods=('GET', 'POST'))
def signup():
    # Creating a form
    myform = forms.SignupForm()

    # If the form has already been filled and the user
    # is sending the data through post
    if flask.request.method == 'POST':
        if myform.validate_on_submit():
            # Retrieving the data from the form
            age  = int(myform.age.data)
            name = myform.name.data
            email = myform.email.data
            pwd  = myform.pwd.data

            # Create a user
            user = models.User(name=name, email=email, age=age, pwd=pwd)

            # Add it to the database
            db.session.add(user)
            db.session.commit()

            # Redirect
            return flask.redirect(flask.url_for('homepage'))

    # It's the first time that the user fetches this page and 
    # we need to send him the page content (the HTML)

    return flask.render_template('signup.jin', form=myform)

@app.route('/profile-update', methods=('GET', 'POST'))
def update_profile():
    form = forms.UpdateProfileForm()
    user = flask_login.current_user
    if user.is_anonymous:
        flask.flash("You need to be logged in to make this action")
        return flask.redirect(flask.url_for('homepage'))

    if flask.request.method == 'POST':
        if form.validate_on_submit():
            status = form.status.data
            name = form.name.data
            age = form.age.data
            email = form.email.data
            user.update_profile(status, name, email, age)

            return flask.redirect(flask.url_for('userpage', user_id=user.user_id))

    # Pre fill form
    form.status.data = user.status
    form.name.data = user.name
    form.age.data = user.age
    form.email.data = user.email

    return flask.render_template('update_profile.jin', form=form)


@app.route('/sign-out')
def signout():
    flask_login.logout_user()
    return flask.redirect(flask.url_for('homepage'))

@app.route('/delete-user/')
def delete_user():
    user = flask_login.current_user 
    flask_login.logout_user(user)
    db.session.delete(user)
    return flask.redirect(flask.url_for('homepage'))


