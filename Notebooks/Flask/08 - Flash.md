# Flash
Flash is a way to render messages to the user.<br>
You can flash a message with `flask.flash(my_message)`

To get those flashed messages you can use `flask.get_flashed_messages()`

In a template, you can display them like this:
{% for message in get_flashed_messages() %}
    <li> {{ message }} </li>
{% endfor %}
For better understanding, you can use `with`
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <li> {{ message }} </li>
        {% endfor %}
    {% endif %}
{% endwith %}