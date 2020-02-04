#!/bin/bash

folder_name=$1
mkdir $folder_name
touch wsgi.py

# Feed wsgi.py
echo "from $folder_name import app" >> wsgi.py
echo "" >> wsgi.py
echo "if __name__ == '__main__':" >> wsgi.py
echo "  app.run(port=5000, debug=True)" >> wsgi.py


cd $folder_name 
touch __init__.py
touch models.py
touch routes.py
touch forms.py
mkdir templates
mkdir static
mkdir static/css
mkdir static/js
mkdir static/pics
touch templates/base.jin
touch templates/homepage.jin

# Feed __init__.py
echo 'import flask, flask_sqlalchemy, flask_migrate' >> __init__.py
echo 'import os' >> __init__.py
echo '' >> __init__.py
echo 'basedir = os.path.abspath(os.path.dirname(__file__))' >> __init__.py
echo 'app = flask.Flask(__name__)' >> __init__.py
echo '' >> __init__.py
echo 'db = flask_sqlalchemy.SQLAlchemy(app)' >> __init__.py
echo 'migrate = flask_migrate.Migrate(app, db)' >> __init__.py
echo '' >> __init__.py
echo 'from platform_app import routes, models' >> __init__.py

# Feed routes.py
echo 'import flask' >> routes.py
echo '' >> routes.py
echo 'from $folder_name import app' >> routes.py
echo '' >> routes.py
echo '@app.route("/")' >> routes.py
echo 'def homepage():' >> routes.py
echo '' >> routes.py
echo 'return flask.render_template('homepage.jin')' >> routes.py
echo '' >> routes.py

# Feed templates/base.jin
echo '<!DOCTYPE html>' >> templates/base.jin
echo '<html lang="en">' >> templates/base.jin
echo '<head>' >> templates/base.jin
  echo '<title>Bootstrap Example</title>' >> templates/base.jin
  echo '<meta charset="utf-8">' >> templates/base.jin
  echo '<meta name="viewport" content="width=device-width, initial-scale=1">' >> templates/base.jin
  echo '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">' >> templates/base.jin
  echo '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>' >> templates/base.jin
  echo '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>' >> templates/base.jin
  echo '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>' >> templates/base.jin
echo '</head>' >> templates/base.jin
echo '<body>' >> templates/base.jin
echo '' >> templates/base.jin
echo '</body>' >> templates/base.jin
echo '</html>' >> templates/base.jin

# Feed homepage.jin
echo '{% extends "base.jin" %}' >> templates/homepage.jin
echo '' >> templates/homepage.jin
echo '{% block main %}' >> templates/homepage.jin
echo '<h1>Hello world, welcome to $folder_name !</h1>' >> templates/homepage.jin
echo '{% endblock %}' >> templates/homepage.jin
echo 'echo "Done"' >> templates/homepage.jin






