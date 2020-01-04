import flask
import datetime

app = flask.Flask("My_first_app")

@app.route('/')
@app.route("/home/<restaurant_name>")
def first_view(restaurant_name):
    food_type       = "Traditional chinese"

    menu = {
        # TITLE: LIST_OF_CONTENT
        'Starters': ['Seviche', 'Focaccia'],
        'Main': ['Beef', 'Vegan beef'],
        'Desserts': ['Chocolate', 'Muffins'],
        'Wine': ['Pepsi', 'Nestle']
    }

    rendered = flask.render_template('restaurant.jin',
                                     restaurant_name=restaurant_name,
                                     food_type=food_type,
                                     menu=menu,
                                    )
    return rendered

@app.route('/welcome/<string:username>')
def welcome(username):
    return "Hello "+username

@app.route('/welcome/<int:age>')
def welcome_age(age):
    return "Hello, {} years old guy!".format(age)

@app.route('/today')
def today():
    today_date = datetime.datetime.now()
    today_date = "{}/{}/{}".format(today_date.day, today_date.month, today_date.year)
    return flask.render_template('today.jin', today_date=today_date)


if __name__ == "__main__":
    app.run(port=5000)

