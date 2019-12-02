### Class and Static methods
Like we saw, python pass the object itself as `self` for every instance method, we can change this also

### Special Methods

You already noticed the weird syntax of the `__init__` method, those four underscores surrounding the method's name are here on purpose, in fact they represent special methods that python automatically call when he needs them.  
For example the `__init__` function is the function that python automatically call when he create an object.  

You can override all those special methods, to make your object act as you want.

##### The `__str__` method

The `__str__` function is the function that python call when he needs to convert an object to a string, for example when printing it.  
For example:  
```python
mylist = [1, 3, 5]
print(str(mylist))
```
Is actually:
```python
mylist = [1, 3, 5]
print(mylist.__str__())
```

##### The `__len__` method

The `__len__` method is here to return the length of the object. It's the method that is called when you try to reach `len(my_object)`.

##### The `__call__` method
One of the most important special methods, it will be used when you try to call the object (meaning adding `()` at the end of the name: `my_object()`).

##### Operators methods

When you use operators like `+` or `-`, there is no magic, python is only executing methods of the object you want to add/substract.  Actually, python use `__add__` and `__sub__` methods.

##### Comparators methods
Operators like `>` and `<` are just calling methods like `__gt__` (greater than) or `__lt__` (less than), here is a list of all the comparators:  
```python
object.__lt__(self, other)  # less then
object.__le__(self, other)  # less or equal
object.__eq__(self, other)  # equal
object.__ne__(self, other)  # not equal 
object.__gt__(self, other)  # greather than
object.__ge__(self, other)  # greater or equal
```
