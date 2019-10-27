# Sequences

Sequence is the generic term for an ordered set. Sequences can be indexable, it means each element can be retrieved with his index, in this way `sequence_name[index_num]`.

> Sequence is not a data type, it's a category of data types



Be careful: **Indexes are starting from 0, and not from 1**

There are other indexing methods:

-  Negative indexes, meaning beginning from the end (`sequence_name[-index_num]`)

- Range indexes, returns a list from an index to the other (`sequence_name[start:end]`)

  > When using ranges, the end index is not included



#### Strings

Actually, `str` is a sequence, it's a sequence of letters. You can index the letters of a string with the indexing technique.

```python
>>> my_name = "Rick"

>>> print(my_name[0])
"R"

>>> print(my_name[2])
"c"

>>> print(my_name[-1])
"k"

>>> print(my_name[1:3])
"ic"
```



#### Lists

List is a collection which is ordered and changeable. It allows duplicate members.

To create a list, use square brackets `[]`, and insert elements, separated by comma `,`. Elements can be every data type. 

For example:

```python
>>> my_hobbies = ["Eat", "Sleep", "Code"]
```

To access the items, refer to the index number.

```python
>>> my_hobbies[0]
"Eat"

>>> my_hobbies[2]
"Code"

>>> my_hobbies[-2]
"Sleep"
```



**Modify an element**

List is mutable, it means the content can be changed, to change an element in a list, refer to the index number and assign a new value.

> **Careful: **Indexes in list start from 0, not from 1

```python
>>> print(my_hobbies)
["Eat", "Sleep", "Code"]

>>> my_hobbies[1] = "Meditate"

>>> print(my_hobbies)
["Eat", "Meditate", "Code"]
```

> Be careful ! If you try to refer to an index that doesn't exist, your program will crash to an `IndexError`



**Add an element**

Adding an element to a list is called appending.

To append an item to a list, use the `append()` method.

```python
>>> print(my_hobbies)
["Eat", "Meditate", "Code"]

>>> my_hobbies.append("Baseball")

>>> print(my_hobbies)
["Eat", "Meditate", "Code", "Baseball"]
```



**Remove an element**

There are several methods to remove items from a list.

- To remove a specified item, use the `remove` method, this method removes the first occurence of the element.

```python
>>> print(my_hobbies)
["Eat", "Meditate", "Code"]

>>> my_hobbies.remove("Meditate")

>>> print(my_hobbies)
["Eat", "Code"]
```



- To remove an item by its index, use the `pop` method, this method removes the element at the given index and returns it.

```python
>>> print(my_hobbies)
["Eat", "Code"]

>>> my_hobbies.pop(0)

>>> print(my_hobbies)
["Code"]
```



**Adding two lists**

Adding two lists will concatenate them.

```python
>>> my_hobbies = ["Food", "Code"]

>>> additional_hobbies = ["Sport", "More code"]

>>> my_hobbies + additional_hobbies 
["Food", "Code", "Sport", "More code"]
```



**Get the length of a list**

To determine how many items a sequence has, use the `len()` method

```python
>>> len(my_hobbies)
2
```

> More on lists [here](https://www.w3schools.com/python/python_lists.asp)


