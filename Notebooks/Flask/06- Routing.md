# Routing

In any programs, you never want to use with hard coded strings, like urls. That's why a lot of routing functions are available from flask.
***

### `flask.url_for`
`flask.url_for` is a flask function that return the url mapped with a given view.<br>
Thus if you change the name of the url in the route decorator of the function, you don't have to change it in every line of code.<br>
`url_for` can also be used in templates.<br>
__Example (create a button that redirect to index):__
<a href="/index"> Index </a>                    // Wrong usage

<a href={{ url_for('index_func') }}> Index </a> // Right usage
For more on `url_for`, see <a href="http://flask.pocoo.org/docs/1.0/api/#flask.url_for">doc</a>
***

### `flask.redirect`
`flask.redirect` function return a response that redirect to another url, you can use it with `url_for`.<br>
__Example of a view that redirect to the index:__


```python
import flask

@app.route("/nowhere")
def redirecting_view():
    return flask.redirect(flask.url_for('index'))
```
