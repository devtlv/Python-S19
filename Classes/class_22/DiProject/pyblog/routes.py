from pyblog import app
import flask

@app.route('/')
def homepage():
    daily_quote = "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live"

    return flask.render_template("homepage.jin", daily_quote=daily_quote)


@app.route("/about-us")
def about():
    return flask.render_template('about.jin')
