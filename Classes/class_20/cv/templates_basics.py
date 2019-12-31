import jinja2

template_str = """
    <html>
        <body>
        <h1>Hello World I am {{ name }} !</h1>

        <h3>Here are my friends names:</h3>

        {% for friend in friends %}
            <p>{{ friend }}</p>
        {% endfor %}

        </body>
    </html>
"""


my_friends = ['Morty', 'Summer']

template = jinja2.Template(template_str)
rendered = template.render(name="Rick", friends=my_friends)

print(rendered)



