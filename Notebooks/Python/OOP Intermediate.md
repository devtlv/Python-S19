### Instance Methods
Instance methods are defined inside a class and are used to define a function that belongs to a class. For example, in real life, the "bark" function belongs t, Dog" class.  
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

### Using objects as addresses

Like functions, objects are just variables containing an address. Understanding this is very important to manipulate objects.  

###### Passing objects as function arguments

The `self` argument is an example of using objects as addresses, it contains the address of the object passed to the function. The `self` argument is not special, his name is just a convention.  
Let's try to pass an object as a function argument, and use it. 

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name,'barks, WOOF!')

def bark_three_times(dog):
    dog.bark()
    dog.bark()
    dog.bark()

my_dog = Dog('Richie')
bark_three_times(my_dog)
```

```python
Richie barks, WOOF !
Richie barks, WOOF !
Richie barks, WOOF !
```

It works ! `my_dog` is just an address, when passed to `bark_three_times`, `dog` argument is taking the value of `my_dog`, so all the operations executed on `dog` are actually executed on `my_dog`.

Actually, everytime you make a function that receives an argument, you are passing an object as argument, but so far it was only built in objects, like string, dict or boolean, python don't know the type of your argument when you are defining the function, you need to check that the input format is respected.

###### Storing objects inside containers

Because they are only variables, you can also store objects in a list, for example, let's create 5 dogs, and store them into a list `my_dogs`.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name,'barks, WOOF!')

def bark_three_times(dog):
    dog.bark()
    dog.bark()
    dog.bark()

my_dogs = [Dog('Richie'), Dog('Tom'), Dog('John'), Dog('Bradley'), Dog('Chocolate')]
```

We don't even need to store each dog in a variable, because they are stored into a list, we can also generate this list dynamically:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name,'barks, WOOF!')

def bark_three_times(dog):
    dog.bark()
    dog.bark()
    dog.bark()

dogs_names = ['Richie', 'Tom', 'John', 'Bradley', 'Chocolate']
my_dogs = []
for name in dogs_names:
    dog = Dog(name)
    my_dogs.append(dog)
```

###### Using an object as an attribute of another object

Let's create a human:
```python
def Human:
    def __init__(self, name):
        self.name = name

me = Human('Rick')
```

Now let's say that this human has a dog, called Richie, first let's create the dog

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name,'barks, WOOF!')

richie = Dog('Richie')
```

We need a way to map between the human and the dog, and this mapping would be even better if it was direct between the human and the dog. Like if `me.dog` was a direct access to the dog object (here called `richie`).  
We can do this, because `richie` is only storing an address, let's just add a `dog` attribute to human.

```python
def Human:
    def __init__(self, name, dog):
        self.name = name
        self.dog  = dog

    def play_with_dog(self):
        print("{} is playing with {}".format(self.name, self.dog.name))
        self.dog.bark()

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name,'barks, WOOF!')

richie = Dog('Richie')
me = Human('Rick', richie)
```
