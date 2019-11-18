# Sets

Sets are another sequence type, it's unordered, it means it does not support indexing, and it doesn't support duplicate too.

> We basically use it to make some list with no duplicates in it

### Defining a set 

To create a set, use the `set()` function

### Add an element to a set

To add an element to a set, use `set.add(element)`

```python
>>> my_set = set()

>>> my_set.add("Rick")

>>> my_set.add("Morty")

>>> my_set.add("Rick")

>>> print(my_set)
{"Rick", "Morty"}
```

### Create a set from a list
You can convert a list to a set, by using the `set()` function, thus you can also create a set from a list:

```python
my_names = set(['Rick', 'Ricky', 'Rrrrrick'])
```

### update
The `add` method can only add one element at the time, while the `update` function can add every elements of a sequence to a set.
```python
my_names = set(['Rick', 'Ricky', 'Rrrrrick'])
my_names.update(['Reack', 'Sancho'])
```



# Tuples

Tuples are immutable lists, it means items can't be changed.

### Defining a tuple

To create a tuple, use parentheses:

```python
>>> my_tuple = (5,6,7)
```

### Modifying tuples
You *cannot* modify a tuple, because a tuple is *immutable*, but you can play with the `+` operator, for example, if you want to append a value to a tuple, you can use the `+=` sign, it won't modify the tuple, else it will create a new tuple and reassign it to your variable:

```python
my_tuple = (5,6,7)
my_tuple += 8
```

### Unpacking tuples
The good thing about tuples is that they can be unpacked, meaning each value will go to one variable:

```python
>>> a, b, c = my_tuple

>>> print(a)
5

>>> print(b)
6

>>> print(c)
7
```


