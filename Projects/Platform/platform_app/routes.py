import flask

from platform_app import app

@app.route("/")
def homepage():

    return flask.render_template('homepage.jin')
