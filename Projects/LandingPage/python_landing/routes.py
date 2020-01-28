from python_landing import app, models
import requests
import flask

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






