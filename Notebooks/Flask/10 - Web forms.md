# What is a form ? 
A web form is a page that allows for user input, by displaying particular fields.

***
# HTML web form

### The `<form>` element
Defines a form to collect user input
### The `action` Attribute
The action attribute defines the action to be performed when the form is submitted.
### The `method` Attribute
The method attribute specifies the HTTP method (GET or POST) to be used when submitting the form data. Default is GET.
### The `target` Attribute
The target attribute specifies if the submitted result will open in a new browser tab, a frame, or in the current window.<br>
The default value is "_self" which means the form will be submitted in the current window.<br>
To make the form result open in a new browser tab, use the value "_blank"
### The `<fieldset>` element
Used to group related data in a form.
<br>
<br>
<a href="https://www.w3schools.com/html/html_forms.asp">More on forms</a>

***
# Flask web form

## First rule: Be lazy,  use packages

WTForms is a python package that generate web forms from models. Flask has a wrapper for it that is called `flask-wtf`, install it.

## Second rule: Protect your site
Once you start to deal with things that are specific to each user (like a form, or a login), you need to encrypt the traffic between your server and the user.<br><br>
Encryption is a hard processus that is handled by flask, but he need one thing, a secret key (a lot of explanations on why are available on internet, for example: see <a href="https://strongarm.io/blog/how-https-works/">This</a>).<br><br>
This secret key has to be defined in the configuration of the app. App configuration is a dictionnary, you can change his entries like in a normal dict (`my_dict[my_key] = value`). <br>
*This should be done in the main python file*


```python
app.config['SECRET_KEY'] = 'you-will-never-guess'
```

    
    

> Even if there is no really reason not to protect your site, you can disable this protection by creating the form with `form = FlaskForm(csrf_enabled=False)`

***
## Create the form
> Forms should be in `forms.py` file

A form is a class than inheritate from `flask_wtf.FlaskForm`. You just have to add fields. Fields are classes too, they can be taken from `wtforms`. <br>
An example of field can be `wtforms.StringField` or `wtforms.PasswordField`, a list can be found on the <a href="http://wtforms.simplecodes.com/docs/0.6/fields.html#basic-fields">wtforms documentation</a>.<br>
Your forms classes dont need an `__init__` method since they already defined it in the parent class, fields should be class variables.<br>
A field definition can have a lot of parameters (See <a href="http://wtforms.simplecodes.com/docs/0.6/fields.html#basic-fields">documentation</a>). Here we will only define the label of the field.


```python
import flask_wtf
import wtforms

class MyForm(flask_wtf.FlaskForm):
    
    name     = wtforms.StringField("Name")
    password = wtforms.PasswordField("Password")
    bio      = wtforms.StringField("Bio")
    submit   = wtforms.SubmitField("Submit")
    
```

### Now that we created the form class, we need to create a template for it
And to add it to a view, we need to create a template for it, in a template, a form acts like a dictionnary, we access the fields with `form.field`, `form.field` can be called, it will display the field:
<form action="" method="post" novalidate>
    {{ form.hidden_tag() }}
    <p>
        {{ form.username.label }}<br>
        {{ form.username(size=32) }}
    </p>
    <p>
        {{ form.password.label }}<br>
        {{ form.password(size=32) }}
    </p>
    <p>
        {{ form.bio.label }}<br>
        {{ form.bio(size=240) }}<br>
    </p>
    <p>{{ form.submit() }}</p>
</form>
### Now we can add it to a view
We first need to import it, and then pass it to the template rendering


```python
from app import app
from app import forms
import flask

@app.route('/myform')
def myform():
    form = forms.MyForm()
    return flask.render_template('myform.html', form=form)
```

### But we need to receive this data
When the form is submitted, the page is refreshed, we can check if the form has been submitted with `validate_on_submit()` function.<br>
Because they are attributes of the form. fields can be received this way `form.fieldname`, they got a `data` attribute that return the input from the user.


```python
from app import app
from app import forms
import flask

@app.route('/myform')
def myform():
    form = forms.MyForm()
    if form.validate_on_submit(): # Check if the form has been filled
        
        username = form.username.data # Get
        password = form.password.data #   The
        bio      = form.bio.data      #     Data
        
        # Do something with the data
        
        return somethin
    return flask.render_template('myform.html', form=form)
```

***
## Focus on fields
Fields are responsible for rendering and data conversion. Doc is available <a href="https://wtforms.readthedocs.io/en/stable/fields.html">here</a>.<br>

### Fields parameters

Fields doesn't need any parameters at creation, but a lot are available (check the doc for exhaustive list).<br>
Examples of parameters are:<br>
-  label: the label of the field
-  validators: the functions that validate the form (check if data was inserted, if it's in the right format..), it should be a list of functions
-  description: description text of the field
-  default: default value of the field
<br>

You can use those parameters in the template, to render their content, for example: <br>
#...

<p> {{ myfield.label }} - {{ myfield() }} </p>
<small> {{ myfield.description }} </small>

#...
### Fields rendering
You can render a field just by calling it, you can add keywords arguments to this call, which will result to be the arguments of the `<input>` tag in the output.

### Basic fields

Here is a little list of some fields from wtforms.fields:
StringField                 - Basic string
PasswordField               - Hidden text field 
BooleanField                - Basically this is a checkbox..
RadioField(choices=[])      - List of radio buttons
SelectField(choices=[])     - List of given choices
FileField/MultipleFileField - file(s) upload fields
SubmitField                 - Submit button
***
## Add validators
A lot of validators are available from `wtforms.validators`, one important is `data_requiered` which raise a `ValidationError` if no data is entered in a field<br>
Every error is stored in a list: `form.field.errors`.<br>
To display them, you need to modify the template.
<br><br>
__Examples of validators:__
validators from wtforms.validators

DataRequired()
Email()
Equalto(another_field)
Length(min, max)
NumberRange(min, max)
Regexp(regex)
Url()
> Note that every wtforms validator can receive a `message` argument, that will be displayed with the error

### Creating a validator

You can create validators as functions (they can be methods of your `Form` class). <br>


```python
def my_length_check(form, field):
    if len(field.data) > 50:
        raise wtforms.ValidationError('Field must be less than 50 characters')
```

All the validators need to receive these two parameters (and only these two parameters): `form` and `field`.<br>

> So how can we add arguments to our validators ? 

<br>
To add arguments, one method is to create a validator creator, the validator will be an inner function of this wrapper.<br>
In simple words, we create a function that receives the arguments, then create the validator, and return the validator function.<br>
Example:


```python
def length(max_len):

    def validator(form, field):
        if len(field.data) > max_len:
            raise ValidationError('Must be between less than {} characters.'.format(max_len))

    return validator
```

Another method is creating the validator as a class, that receives argument at definition, and use them on call. When you call an object, you actually call `object.__call__()`


```python
class MaxLengthValidator(object):
    def __init__(self, maxlen, message=None):
        self.max_len
        if not message:
            message = 'Field must be less than {} characters.'.format(max_len)
        self.message = message

    def __call__(self, form, field):
        if len(field.data) > self.max_len:
            raise ValidationError('Must be between less than {} characters.'.format(max_len))
```
