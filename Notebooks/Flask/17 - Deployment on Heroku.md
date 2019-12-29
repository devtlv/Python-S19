# Heroku
Heroku is a Platform as a Service (A cloud platform) hosting that supports python. 

### Requirements to deploy your app on heroku

To deploy on heroku, you first need to have a requirements.txt file, this is a file that define every module needed by your program. To automatically create one, you can install pipreqs (`pip install pipreqs`) and run `pipreqs .` in your project folder.  
Your project needs also to be a git repository, you can do this by running `git init` in your project folder.  
Now the last thing you need is a [heroku account](https://signup.heroku.com/)

### Installing the Heroku Command Line
To manage Heroku apps directly from the terminal, you can use the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). To verify your installation, type `heroku --version` in your terminal.

### Login 
Now that the CLI is installed, you need to login to your heroku account by typing:  
`heroku login`   


### Procfile

The procfile is a file of commands that is executed when you run your server.  
It needs to be created in the root directory of your application.  
Here is the format of each line in the file:  

```bash
<process_name>: <command>
```  

To start a web application, the `process_name` should be `web`. If you need to add more than one command, just separate them with a semi-colon `;`.

Here is an example of a procfile:

web: flask db upgrade
### Create an app
After you logged in, you can create an app by running:  
```bash 
heroku apps:create <name_of_the_app>
```
> Be sure to be in your project folder when you run this, to do so, run `cd path/to/project`, to check your current folder, type `pwd` on linux and `echo %cd%` on windows

### Create a database
SQLite is good for developement, but shouldn't be used for deployed site. Instead of this, use other SQL databases like MySQL or PostgreSQL.  
To install Postgres support on heroku, run this in your terminal:  
```bash
heroku addons:create heroku-postgresql:hobby-dev
```  
The path to the database will be stored in the `DATABASE_URL` environnement variable, thus we can delete the `SQL_DATABASE_URI` from the config.  
To work with postgres, you need a little module, called psycopg2, to install it, run `pip install psycopg2` (if the installation doesn't work, that's ok, anyway it was not supposed to run on your local computer, heroku will install it)
> Don't forget to put psycopg2 in your requirements file



### Logs

Logs are records of your program's output, when you have a weird behavior, you take a look at the logs to understand what happened (it's the output you see on your terminal while running your flask app).  
You can run `heroku logs` to retrieve them.

### Create an environnement variable
Sometimes you need to create a new environnement variable (like `FLASK_APP` if your application isn't named `app.py` or `wsgi.py`), to do so in heroku, just run 
```bash 
heroku config:set <variable_name>=<variable_value>
``` 

### Creating a web server
A web server is a program that manage HTTP requests, we already know how to create one. Actually we run a web server each time we run `flask run`, but this web server is not good for production because it's not optimized.  
Thus we will use another python web server, that is also very popular, called gunicorn (to install: `pip install gunicorn`).  
To run a flask application with gunicorn on heroku, you need to run this command:  
```bash
gunicorn <file_name>:<variable_name>
```  

This command should be in the procfile, on my computer, my runner file is called `wsgi.py` and inside it I run `app.run(port=5000)`, so the variable is called `app`, thus I'll put this in my procfile:

web: flask db upgrade; gunicorn wsgi:app
> Notice That the 

### Deploy !

Here it is, the final step !  

To send your app to the server, you need nothing more than git.  
First, be sure to add all your changes with  
```bash
git add .
git commit -m "heroku deployment"
```   

And then push it to the heroku server, heroku automatically adds the server as a remote repository, with `heroku` as label, so just run:  
```bash 
git push heroku master
```  

Here you are, your server is running, run `heroku logs` to see the output of your app.
   _____                 _     _       _       _ 
  / ____|               | |   (_)     | |     | |
 | |  __  ___   ___   __| |    _  ___ | |__   | |
 | | |_ |/ _ \ / _ \ / _` |   | |/ _ \| '_ \  | |
 | |__| | (_) | (_) | (_| |   | | (_) | |_) | |_|
  \_____|\___/ \___/ \__,_|   | |\___/|_.__/  (_)
                             _/ |                
                            |__/                 