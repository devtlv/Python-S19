# Control flow 

#### Conditions

Conditions are expressions that compare two elements.

Python support the following logical conditions:

- Equals: `a == b`

- Not Equals: `a != b`

- Less than: `a < b`

- Less than or equal to: `a <= b`

- Greater than: `a > b`

- Greater than or equal to: `a >= b`

  

Those expressions return True or False 

```python 
>>> 33 > 20
True
>>> 130 > 190
False
```



**if statements**

`if` statement test a condition, and execute a code if the condition is True.

Here is the syntax: 

```
...
if <condition>:
    CODE
    CODE
...   
```



>  Notice that python relies on indentation (whitespace at the beginning of a line) to define scope in the code.

```python
a = 33
b = 200
if a > b:
    print("a is greater than b")
    
print("Finished")
    
```

> Test this code with some other values !



**elif statement**

The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

```python
a = 33
b = 200

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

print("Finished")
```



**else statement**

The `else` keyword catches anything which isn't caught by the preceding conditions.

```python
a = 33
b = 200

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")
    
print("Finished")
```



**AND & OR statements**

They are both used to combine conditional statements.

`and` statement will be activated if both conditions are true

```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
```

`or` statement will be activated if only one of the condition is true

```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```



**in keyword**

`in` keyword can be used to check if a value is in a sequence.

The expression `my_var in my_list` is a boolean, it will be replaced by `True` or `False`

```python
>>> 8 in [1,2,3,4,5]
False

>>> "A" in "ABCD"
True
```



```python
my_hobbies = ["sport", "code", "food", "icecreams", "netflix"]
if "code" in my_hobbies:
    print("Hello world")
```



#### not keyword

The `not` keyword will just return `True` if the condition is False.