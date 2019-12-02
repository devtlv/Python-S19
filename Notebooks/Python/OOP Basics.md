# Object Oriented Programming

***
### Abstract

Object-oriented Programming, or OOP for short, mean structuring programs so that properties and behaviors are bundled into individual objects.  

For instance, an object could represent a person with a name property, age, address, etc., with behaviors like walking, talking, breathing, and running. Or an email with properties like recipient list, subject, body, etc., and behaviors like adding attachments and sending.

Put another way, object-oriented programming is an approach for modeling concrete, real-world things like cars as well as relations between things like companies and employees, students and teachers, etc. OOP models real-world entities as software objects, which have some data associated with them and can perform certain functions. 

### Classes

Focusing first on the data, each thing or object is an instance of some class.  

The primitive data structures available in Python, like numbers, strings, and lists are designed to represent simple things like the cost of something, the name of a poem, and your favorite colors, respectively. But what if you wanted to represent something much more complicated?  


For example, let’s say you wanted to track a number of different animals. If you used a list, the first element could be the animal’s name while the second element could represent its age. How would you know which element is supposed to be which? What if you had 100 different animals? Are you certain each animal has both a name and an age, and so forth? What if you wanted to add other properties to these animals? This lacks organization, and it’s the exact need for classes.

Classes are used to create new user-defined data structures that contain arbitrary information about something. In the case of an animal, we could create an `Animal` class to track properties about the Animal like the name and age.   

It’s important to note that a class just provides structure—it’s a blueprint for how something should be defined, but it doesn’t actually provide any real content itself. The `Animal` class may specify that the name and age are necessary for defining an animal, but it will not actually state what a specific animal’s name or age is. It may help to think of a class as an idea for how something should be defined.

### Objects (instances)

While the class is the blueprint, an instance is a copy of the class with actual values, literally an object belonging to a specific class. It’s not an idea anymore; it’s an actual animal, like a dog named Roger who’s eight years old.

Put another way, a class is like a form or questionnaire. It defines the needed information. After you fill out the form, your specific copy is an instance of the class; it contains actual information relevant to you.

You can fill out multiple copies to create many different instances, but without the form as a guide, you would be lost, not knowing what information is required. Thus, before you can create individual instances of an object, we must first specify what is needed by defining a class.

***

### Defining a class
Defining a class is simple in Python:
```python
class Dog():
    pass
```
You start with the `class` keyword to indicate that you are creating a class, then you add the name of the class (using *CamelCase* notation, starting with a capital letter.)

Also, we used the Python keyword `pass` here. This is very often used as a place holder where code will eventually go. It allows us to run this code without throwing an error.

### Creating an object (instance)
Like we said, class is only a blueprint, to create an object, or an instance, of this class, you simply want to *call* the class.
```python
class Dog():
    pass

my_dog = Dog()
```
Here we created `my_dog`, which is an object of the class `Dog`.


### Attributes
Even in the real life, all objects have attributes, for example, dogs have **height**, **color** and **race**, we can implement this in our classes so all the objects of a same class have the same attributes (though not the same values for those attributes).  

Attributes are like variables, they can be any data type, the only difference is that they belong to an object.  

To target an attribute, you need to refer to the object (`my_dog`), followed by a dot `.` and the name of the attribute. For example
```python
dog.color
```
This will refer to the `color` attribute of the dog. Of course, when you are trying to target an object's attribute, you need to target an existing attribute, else you will have an error.  

To define a new attribute (or modify an existing one), just target it and assign it to his new value with the equal sign `=`.   
```python
class Dog():
    pass

my_dog = Dog()
my_dog.color = "Brown"
```

### Class Method

```python
class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        print(self)

computer_obj = Computer()
computer_obj.brand = "Razer"

computer2 = Computer()
computer2.description('Eyals friends computer')

Computer.description(computer_obj, "Eyal's PC")
# IS THE SAME AS:
computer_obj.description("Eyal's PC")
```



### The `__init__` method

When an object is created, python automatically run the `__init__()` (it has to be called like that) method of the class.  
This method must have at leat one argument, `self` (it doesn't have to be called `self` but that is a python convention), `self` refers to the object itself.

```python
class Dog():

    # Initializer / Instance Attributes
    def __init__(self):
        print("A new dog has been initialized !")

my_dog = Dog()
```
Although this function receive one argument (`self`), we don't need to pass it, it will be passed automatically by python as first argument.  

You can add arguments to `__init__`, those arguments would be the ones passed on the object creation (`my_dog = Dog()`).   
For example:   
```python
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)

my_dog = Dog(name_of_the_dog="Rex")
# or
my_dog = Dog("Rex")
```
Here we are passing only one argument (`"Rex"`), but in fact, two values are passed, the `name_of_the_dog` and `my_dog` itself, as `self`. In fact this is what python is running:
```python
my_dog = Dog(my_dog, "Rex")
```
This argument is passed *implicitly*.  

Most of the time, you want to initialize the attributes of an object on his creation (like a new born dog would have some initial color, race and height..).  
To do so, you can pass arguments to the `__init__()` function, and then initialize attributes in the function.  
Remember that to assign a value to an attribute we need to select the attribute with `object.attribute` and assign it with the `=` sign. In `__init__` function, the object is refered as `self`, thus to define an attribute you need `self.attribute = value`.  

```python
class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)
        self.name = name_of_the_dog

my_dog = Dog('Rex')
my_other_dog = Dog("Jimmy")
```

Here I have created two different `Dog` objects, with two different names.  
