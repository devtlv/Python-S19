### Instance Methods
Instance methods are defined inside a class and are used to define a function that belongs to a class. For example, in real life, the "bark" function belongs to "Dog" class.  
Instance methods can be used to perform operations with the attributes, or to get the contents of an instance, and many other things.   

To define a method, just use the `def` keyword inside the class, like we were doing with the `__init__` method. All instance methods need to receive `self` as first argument, this allow us to play with the object inside the method.  

Let's define the bark method.  
```python
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))
```

To call an instance method, just type the name of the instance (object) followed by a dot `.` and the name of the function. Let's create a `Dog` object and call the `bark` function.  

```python
my_dog = Dog("Rex")
my_dog.bark()
```

The first line will output:
```python
A new dog has been initialized
His name is Rex
```

And the second:
```python
Rex barks ! WAF
```

The methods can also receive arguments, after the `self` one, which will be passed implicitly.

```python
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

my_dog = Dog("Rex")
my_dog.walk(10)
```

You can also use instance methods to modify object's attributes.  
Here is a function that change the dog's name:

```python
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog.rename("Paul")
```

Remember that the `self` keyword refers to the object itself.  

### Class Attribute
You can also define an attribute that belongs to the class and not to each instance, it's called a class attribute.  
For example, let's define the name of dogs's king as a class attribute:

```python
class Dog():
    dogs_king = "Bernie IV"

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog.rename("Paul")
```

The `dogs_king` variable is now defined as "Bernie IV", we don't need to have a `Dog` object to call this variable, just use:  
```python
print("The king of the dogs is:", Dog.dogs.king)
```

For example, we can save the number of dogs ever created in a class variable, and increment it each time a dog is created (in the `__init__` function).  

```python
class Dog():
    number_of_dogs = 0
    dogs_king = "Bernie IV"

    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog
        # Increment the number of dogs
        Dog.number_of_dogs += 1

    def bark(self):
        print("{} barks ! WAF".format(self.name))

    def walk(self, number_of_meters):
        print("{} walked {} meters".format(self.name, number_of_meters))

    def rename(self, new_name):
        self.name = new_name

my_dog = Dog("Rex")
my_dog2 = Dog("Bernie V")
print("Curently, there are {} dogs".format(Dog.number_of_dogs))
```

### Inheritance

Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.   

In real life for example, Dog is a child class of Animal, every Dog is an Animal, but every Animal isn't a Dog. Child inherit all of the parent's attributes and behaviors but can also specify different behavior to follow.  

To make a class inherit from another one, simply add it in round brackets on class definition:

```python
class Animal():
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))

```

It’s important to note that child classes override or extend the functionality of parent classes. The child class will have all the parent class's functions, plus his own functions.

A class can inherit from 2 classes, in this case the order of the parents class in the class definition will matter, the firsts ones will have a priority on the last ones (it means their functions will override the others's ones).


```python
class Alien():
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def fly(self):
        print(self.name, 'is flying!')

    def sleep(self):
        print("Aliens don't sleep")

class Animal():
    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("zzzZZZZZ")

class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))

class AlienDog(Alien, Dog):
    def bark(self):
        print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.name))

my_dog = AlienDog("Rex", "Lithis04")
```

Here I have created two new classes, `Alien` and `AlienDog`, `AlienDog` inherit from `Alien` and from `Dog`, but both classes have an `__init__` and a `sleep` method, though the functions of `Alien` will be transfered to `AlienDog` because `Alien` is before `Dog` in the class definition (`class AlienDog(Alien, Dog)`).

