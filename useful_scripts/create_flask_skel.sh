#!/bin/bash

mkdir app_folder
touch wsgi.py

echo "from app_folder import app" >> wsgi.py
echo "" >> wsgi.py
echo "if __name__ == '__main__':" >> wsgi.py
echo "  app.run(port=5000, debug=True)" >> wsgi.py


cd app_folder
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

echo "import flask" >> __init__.py
echo "import os" >> __init__.py
echo "" >> __init__.py
echo "basedir = os.path.abspath(os.path.dirname(__file__))" >> __init__.py
echo "app = flask.Flask(__name__)" >> __init__.py


echo "Done"






