# Numbers and Strings in python 

Numbers and words are two differents data types in python. 

Numbers are called integers, or `int`.

Words are called strings, or `str`. 

Python recognize `str` data type when he sees quotation marks `"`, for example:

`"Hello world"` is a valid string

`Hello world` is not a valid string 

> Be careful ! `Hello world` will crash your program, because python won't recognize it at all

#### Check a data type
To check the type of an element, pass it to the `type` function. For example:
```python
>>> type(30)
<class 'int'>

>>> type('30')
<class 'str'>
```


#### Converting to another data type

You can convert some data from a type to another by using the `int` or the `str` function. For example, to convert `30` into a string, use:

```python
>>> str(30)
"30"
```

And in the other way:

```python
>>> int("30")
30
```

> Notice the quotation marks `"`, they are here to specify that data is `str` 



#### Adding data types together

You can add a string with a string, and a number with a number, but not a number with a string. 

Adding two string will stick them together, time it by 4 will make 4 copies of it.

For example:

```python
>>> "Hello" + "World"
"HelloWorld"

>>> "Hello "*4
"Hello Hello Hello Hello "

>>> "Hello" + " " + "World"
"Hello World"

>>> ("Hello" + "World" + " ")*2
"HelloWorld HelloWorld "
```

Trying to add a string with a number will throw an error:

```python
>>> "My favourite number is " + 8
Traceback (most recent call last):                                                                                      File "<stdin>", line 1, in <module>                                                                                 TypeError: unsupported operand type(s) for +: 'int' and 'str'  
```

> Notice that the error has a type `TypeError` and a clear explanation `Unsupported operand type(s) for +: 'int' and 'str'` 



#### Special characters

For a computer, everything is a character, even tabs and new lines, to define a new line in python, use the `\n` character, for a tab, use the `\t` character. For example:

```python
>>> print("Hello world\nMy name is Rick")
Hello world
My name is Rick

>>>print("Peace on the\tWORLD")
Peace on the 	WORLD
```

# Booleans

Booleans (`bool`) are another python data type, they are used to represent truth values (`True` or `False`). 

In numeric contexts, they behave like 1 and 0.

To convert a variable to boolean, use the `bool()` function.

When converted, a variable is set as `True` if it's not `None`, `0` or `False` .

For example, a result of a python comparaison (for example: `5 > 3`) is a boolean, it will be replaced by `True` (if the condition is true) or `False` (if the condition is false).
