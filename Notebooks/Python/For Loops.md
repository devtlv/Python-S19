

# For loops

You’ll often want to run through all entries in a list, performing the same task with each item. 

When you want to do the same action with every item in a sequence, you can use Python’s `for` loop.

First, the syntax: 

```
for <variable_name> in <sequence_name>:
	CODE
	CODE
```

> Notice the usage of colon `:` and the indentation of the code.



Let's understand this with an example:

```python
cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]

for city in cities:
    print("I once went to", city)
```

The first line of the loop is:

```
for city in cities:
```

This line tells Python to retrieve the first value from the list `cities` and store it in the variable `city`.

The name `city` can be anything else, if this variable don't exist, it will be created, else its value will be replaced by the first value of `cities`. You can choose any name you want for this variable, however, it’s helpful to choose a meaningful name that represents a single item from the list.

 This first value is 'Tel Aviv'. Python then reads the next line:

```
    print("I once went to", city)
```

Python print the value of `city`, which is 'Tel Aviv'. Because the list contains more values, he returns to the first line.

```python
for city in cities:
```

Python now retrieves the next element of the list, and store it in the variable `city` (his value is over-written).

```
	print("I once went to", city)
```

Now python will print `I once went to San Francisco`.

...

Python continues like this until he reaches the end of the list.



#### Making numerical lists

Python’s range() function makes it easy to generate a series of numbers. For example, you can use the range() function to print a series of numbers like this:

```python
for number in range(1,5):
    print(number)
```

```
1
2
3
4
```

The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. 

Because it stops at that second value, the output never contains the end value, which would have been 5 in this case. 

> To print numbers from 1 to 5, use `range(1,6)`



Although it can be iterated, the result of `range` is not a `list`, to store it in a `list`, you can convert the results of `range()` directly into a `list` using the `list()` function. When you wrap `list()` around a call to the `range()` function, the output will be a list of numbers.

```python
numbers = list(range(1,6))
print(numbers)
```



#### Some built in functions that use for loops

Functions like `min`, `max` or `sum` are using for loops behind the scenes, to practice, you can try to program them by yourself.



#### Avoiding indentation errors

Python uses indentation to determine when one line of code is connected to the line above it. 

In the previous examples, the lines that printed messages on every city were part of the for loop because they were indented.

Python’s use of indentation makes code very easy to read. 





