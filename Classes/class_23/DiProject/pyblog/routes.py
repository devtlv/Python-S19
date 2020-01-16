from pyblog import app, db
from pyblog import models, forms
import flask

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

@app.route("/sign-up", methods=('GET', 'POST'))
def signup():
    # Creating a form
    myform = forms.SignupForm()

    # If the form has already been filled and the user
    # is sending the data through post
    if flask.request.method == 'POST':

        # Retrieving the data from the form
        age  = int(myform.age.data)
        name = myform.name.data
        pwd  = myform.pwd.data

        # Create a user
        user = models.User(name=name, age=age, pwd=pwd)

        # Add it to the database
        db.session.add(user)
        db.session.commit()

        # Redirect
        return flask.redirect(flask.url_for('homepage'))

    # It's the first time that the user fetches this page and 
    # we need to send him the page content (the HTML)
    else:

        return flask.render_template('signup.jin', form=myform)














