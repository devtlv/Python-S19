# Templates?

Templates are a way to generate dynamic html code. Meaning adding variables, for loops and if statements to the HTML code.
The template is written in a template language which combines python and HTML. <br>
There a lot of python modules that can convert template to html code (called template engines), flask use __jinja2__

> Templates can be stored with every extension

# Delimiters

-  __{%....%}__ are for statements
-  __{{....}}__ are expressions used to print to template output
-  __{#....#}__ are for comments which are not included in the template output

# Deal with no indentation

Because html doesn't support indentation, we close the statements with an __{% endstatement %}__ 

***

# Variables

&lt;p> Hi {{ name }}, how are you today? &lt;/p>

# Statements

## if statement
<pre><code>
{% if name == "Eyal" %}
    &lt;p> Hello Eyal &lt;/p>
{% else %}
    &lt;p> Who are you ? &lt;/p>
{% endif %}
</pre></code>

## for statement
<pre><code>
{% for name in ["Eyal", "Mario", "Luigi"] %}
    &lt;p> Hello {{ name }} &lt;/p>
{% endfor %}
</pre></code>

# Template inheritance

A lot of times, the base of the site is the same, templates enable us to create a Parent template with a fillable part that can be filled with a Child template.

## Add a fillable block of code
<br>
### In the parent template
__{% block %}{% endblock %}__ remain a part of code empty in a template<br>

### In the child template
In the child template, you need to specify that you are extending the parent template, with __{% extends "name_of_the_template.html" %}__.<br>
Then you need to open the __{% block %}__ tag and write the code that have to be injected to the Parent template <br>

>You can add more than one block, and then give them a name with __{% block blockname %}{% endblock %}__

***
# Transform template to HTML code

`flask.render_template_string` is a flask function that can render a template to html code. The template needs to be filled with variables, that need to be injected into that function.<br>
__Example:__ `flask.render_template_string(my_template, name="Eyal")`<br>
> A template can also be rendered from a file, with `flask.render_template(file, args)`, the files need to be in a `templates/` folder
