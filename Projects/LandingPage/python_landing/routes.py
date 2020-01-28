from python_landing import app
import flask

@app.route('/')
def homepage():
    return flask.render_template('homepage.jin')

@app.route('/news')
def news():
    news = [
        "Python 3.8 just came out !",
        "You can now use := operator",
        "This site is made with flask"
    ]

    return flask.render_template('news.jin', news=news)

@app.route('/forum')
def forum():

    return flask.render_template('forum.jin')




