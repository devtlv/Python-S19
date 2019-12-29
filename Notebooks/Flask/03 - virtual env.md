# Virtualenv

Imagine you have an application that needs the version 3 of beautiful soup, and another that needs the version 2, how can you use both of these applications ? 

### What is virtualenv ?
Virtualenv is a tool which allows us to make isolated python environments. It allows you to install packages inside it.

### Installing virtualenv
Installing virtualenv can be done with *pip*<br>
> `$ pip install virtualenv`

*** 
### Using virtualenv

First, we need to create a virtual env, this can be done with:<br>
> `$ virtualenv my_environnement`<br>

And then we just need to activate it by running: <br>
> On unix: `$ source my_environnement/bin/activate`<br>
> On Windows: `$ my_environnement/Scripts/activate`

To deactivate it:
> `$ deactivate`

***
See: <a href="https://docs.python-guide.org/dev/virtualenvs/">Virtualenv documentation</a>
