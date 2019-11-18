# Dictionnaries

`Dictionnary` is a data type provided by python, which is another collection of objects.  

A dictionary is similar to a list, in many ways:  
-  It's mutable (his elements can be changed)
-  It's dynamic (it can grow as needed)

The only real difference between dictionaries and lists is how elements are accessed:  
In lists, elements are accessed by their position in the list (via indexing), for example:
```python
my_list = ['Rick', 'Sanchez']
print("My last name is:",my_list[1])
```
To access the word `"Sanchez"`, we need to put his index in the square brackets `[]`.  

In dictionaries it's a bit different, elements have no index, they are accessed via keys. A dictionary is basically an associative array, it consists of a collection of key-value pairs. Each key=value pair maps the key to its associated value (for example, the key `first name` is associated to `Rick` and the key `last name` is associated to `Sanchez`).

#### Define a dictionary

While lists are defined by square brackets `[]`, dictionaries are defined by enclosing a list of key-value pairs in curly braces `{}`.  
A colon `:` is used to separate each key from its associated value:
```python
my_dict = {
    <KEY1>: <VALUE1>,
    <KEY2>: <VALUE2>,
    <KEY3>: <VALUE3>
}
```

```python
rick_dict = {
    'first name':'Rick',
    'last name':'Sanchez'
}
```

#### Accessing dictionary values
To access a dictionary elements, you need to specify its corresponding key, in the exact same way that you're specifying the index of an element in a list, in square brackets `[]`.  
For example:
```python
rick_dict = {
    'first name':'Rick',
    'last name':'Sanchez'
}
print("The last name of rick is:", rick_dict['last name'])
```

If you refer to a key that is not in the dictionary, you will get an error:
```python
print("The last name of rick is:", rick_dict['age'])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    rick_dict['age']
KeyError: 'age'
```

#### Modify an entry in a dictionary
Modifying an element in a dictionary works the same as a list, first you need to select it (with his key) and then assign it to a new value with the equal sign `=`.  
```python
rick_dict['last name'] = 'SANCHEZ'
```


#### Adding an entry to an existing dictionary
To add an entry to an existing dictionary, just assign a new key to its value, like you would have modify it if it was an existing key.
```python
rick_dict['hair color'] = 'white'

```

#### Delete an entry in a dictionary

To delete an entry, use the del statement, specifying the key to delete:

```python
del rick_dict['hair color']
```

#### Keys restrictions

Almost any type of value can be used as a dictionary key in Python. But there are a couple restrictions.

-  First, keys are uniques, they can appear in a dictionary only once, if you assign a value to an existing dictionary key, it does not add the key a second time, but replace the existing value.
-  Secondly, key must be a type that is immutable, it can be an integer, a float, a string, a boolean, and even a tuple, because all those types are immutables. List can't be a dictionary key.

By contrast, there are no restrictions on dictionary values.

#### The `in` keyword
In a list, the `in` keyword return `True` or `False` according to wheter the specified operand occurs in the list.  
For a dictionary, it returns `True` if the operand occurs **as a key** in the dictionary.

#### Built in methods

###### `keys()`
The `my_dict.keys()` method returns a list of all the keys in `my_dict`

###### `values()`
The `my_dict.values()` method returns a list of all the values in `my_dict`

###### `items()`
The `my_dict.items()` method returns a list of tuples containing the key-value pairs in a dictionnary.
```python
rick_dict = {
    'first name':'Rick',
    'last name':'Sanchez'
}
print(rick_dict.items())
```

###### `update(<key>)`

If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:

-  If the key is not present in d, the key-value pair from <obj> is added to d.
-  If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.



