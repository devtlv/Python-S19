# Variables in python

Variables are containers for storing data value. Every variable has a name and a value, the value can be any data type.

When python read the name of a variable, he simply replace it by its value.

Declaring a variable is really easy: `variable_name = "variable value"`, for example:

```python
my_name = "Rick"
my_age  = 43
```



#### Variable names

Variable names need to follow some conventions, written in a documentation called [PEP 8](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names). This documentation is defining all the standards that your code should follow. 

Variable names should:

-  Be composed only of lowercase letters or numbers, with words separated by underscores
- Never start with a number
- Be easy to read and understand
- Not be one of the [python keywords](https://www.programiz.com/python-programming/keywords-identifier)



#### Using variable

To use a variable, just type his name, and python will replace it by his value.

```python
>>> my_age  = 43

>>> my_name = "Rick"

>>> "My name is " + my_name + " and I am " + my_age + " years old"
"My name is Rick and I am 43 years old"
```

#### Display the value of a variable

To display a variable's value, you can use the `print` function. For example:

```python
>>> my_hair_color = "black"

>>> print(my_hair_color)
"black"
```

You can also pass more than one argument to `print`, they should be separated by a comma `,`. Python will print all the items separated by a space. For example:

```python
>>> print("My hair is", my_hair_color)
"My hair is black"
```



#### Increment a variable

Incrementing means "Adding one to", to increment a variable, just replace his value by "itself plus one":

```python
my_number = 5

# Increment it
my_number = my_number + 1

# Now my number is 6
```

This can be resume to

```python
my_number = 5

my_number += 5 
# += means "= my_number +"
```

This syntax can be used with **every operator**.



#### String formatting

Sometimes writing a string with a lot of variables in it is hard, that's why we use *string formatting*. Every string variable has a `format` function that work in this way:

This function work by putting in one or more replacement fields and placeholders defined by a pair of curly braces `{}` into a string and calling the `str.format()` function. The value we wish to put into the placeholders and concatenate with the string passed as parameters into the format function.

For example:

```python
>>> birthday_day = "08"

>>> birthday_month = "02"

>>> birthday_year = "1979"

>>> print("I was born the {}/{}/{}".format(birthday_day, birthday_month, birthday_year))
"I was born the 08/02/1979"
```

> Be careful, the number of `{}` needs to be equal to the number of given arguments



 #### Why should we use variables ?

Variables are here to make your code dynamic, when programming, you want to be able to run the same piece of code but with different values, that's why variables were created for.
