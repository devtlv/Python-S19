# Database relationships

For a minute, forget about the database models, let's take a simple class as example.<br>
Let's take the example of a `Human` object, which have a d.og.<br>
The dog is assigned to the human, it's an attribute of the human.<br>
The question is, what do we need to put in the human class, as `self.dog` ? <br>
The dog's name ? <br>
The dog's race ? <br>
<br>
The best thing to do is to assign a whole entity to `self.dog`, a entire `Dog` object.<br>
__For example:__


```python
class Human:
    def __init__(self, name):
        self.name = name 
        self.dog  = None  # Currently, the human has no dog
    
    def add_dog(self, dog):
        self.dog = dog
        
class Dog:
    def __init__(self, name, race):
        self.name = name
        self.race = race
    
    def bark(self):
        print("Woof!")
        
my_human = Human("John")
my_dog   = Dog("Rex", "Bulldog") 

my_human.add_dog(my_dog)
my_human.dog.bark()
        
```

    Woof!
    

Here we added an dog object to the human object, in fact `self.dog` is an address, the address of `my_dog`, we can checking by typing:


```python
print(my_dog)
print(my_human.dog)
```

    <__main__.Dog object at 0x7fc98c411278>
    <__main__.Dog object at 0x7fc98c411278>
    

We can see that `my_dog` and `my_human.dog` are the same addresses, inserting a object address in an object attribute is called a `foreign key`. The last thing that we need to do is assigning the human to the dog.


```python
class Human:
    def __init__(self, name):
        self.name = name 
        self.dog  = None  # Currently, the human has no dog
    
    def add_dog(self, dog):
        self.dog = dog
        dog.human = self
        
class Dog:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        
        self.human = None
        
    def bark(self):
        print("Woof!")
        
my_human = Human("John")
my_dog   = Dog("Rex", "Bulldog")

my_human.add_dog(my_dog)
my_human.dog.bark()

print(my_dog.human)
```

    Woof!
    <__main__.Human object at 0x7fc98c411828>
    

## One-to-one
A one-to-one relationship is a relation between two single objects, here, every dog has one human and every human has one dog.<br>

## One-to-many
Consider a human that can have more than one dog.<br>
The class will look like this:<br>


```python
class Human:
    def __init__(self, name):
        self.name = name 
        self.dogs  = []  # Currently, the human has no dog
    
    def add_dog(self, dog):
        self.dogs.append(dog)
        dog.human = self
        
class Dog:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        
        self.human = None
        
    def bark(self):
        print("Woof!")
        
my_human = Human("John")
my_dog   = Dog("Rex", "Bulldog")
my_dog2  = Dog("Cookie", "Chinchilla")

my_human.add_dog(my_dog)
my_human.add_dog(my_dog2)

for dog in my_human.dogs:
    dog.bark()

print(my_dog.human)
```

    Woof!
    Woof!
    <__main__.Human object at 0x7fc98c38d1d0>
    

Here, every dog has one human but every human has many dogs, it's called a `One-To-Many` relationship.

***
# In flask, it can be translated with `db.relationship`:


```python
from app import db

class Human(db.Model):
    id   = db.Column(db.Integer)
    name = db.Column(db.String(64), index=True, unique=True)
    dogs = db.relationship('Post', backref='human', lazy='dynamic')

class Dog(db.Model):
    name = db.Column(db.String(64), index=True)
    race = db.Column(db.String(64))
    master = db.Column(db.Integer, db.ForeignKey('human.id'))

```

In the human side, we are adding a `db.relationship` field, this is a field that represent a link with another object, `backref` is the name of the attribute that represents the human in the dog class.<br>
For example, declaring a dog:<br>


```python
my_human = Human(name="John")
my_dog = Dog(name="Rex", race="Chinchilla", human=my_human)
```

In the dog side, we added a master field, that is linked to the `name` field of the human, which is precised by the `db.ForeignKey` argument.

# SQLAlchemy relationship
This field can link two tables.<br>
`db.relationship` create a new table that map every object with his related objec, while `ForeignKey` is just a pointer to one external object.<br><br>
In the parent class (the ONE side), we need to create a `db.relationship` attribute that will point to the object.<br>
In the child class (the MANY side), we add an Integer column, with a `ForeignKey` as argument, this will be the reference for tthe parent object.
<br>
By default, `db.relationship` is a `List`, we can modify it by setting `uselist` argument as `False`, the field will then be a single element.
<br>
Other tables can be created, like One-To-One or Many-To-One.

***
# Many-To-Many 

Both sides can have many relationships, an example can be the `picture/user` relationship on instagram, every user like many pictures and every pictures has many likes.<br>
To create this kind of relationship, we need to create a table that maps the different objects. The table should be a <a href="https://docs.sqlalchemy.org/en/13/core/metadata.html#sqlalchemy.schema.Table">`Table`</a> object. This table should be created independantly of the models.


```python
from app import db
dogs_table = db.Table('dogs',
                      db.Column('human_id', db.Integer, db.ForeignKey('human.id')),
                      db.Column('dog_id', db.Integer, db.ForeignKey('dog.id'))
)
```

The relationship is now taking the table as <a href="https://docs.sqlalchemy.org/en/13/orm/relationship_api.html#sqlalchemy.orm.relationship.params.secondary">`secondary`</a> argument, which represents the intermediary table.


```python
class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dogs = db.relationship("Dog", secondary=dogs_table)
    
class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
```

***
# Bidirectional relationship
Here, the relationship is only stored in one of the classes, the parent one, if you want a bidirectionnal relationship, you can add a relationship in the child class and add the <a href="https://docs.sqlalchemy.org/en/13/orm/relationship_api.html#sqlalchemy.orm.relationship.params.back_populates">relationship.back_populates</a> argument, the value of this argument should be the relationship field name in the other class.


```python
class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dogs = db.relationship("Dog", secondary=dogs_table, back_populates="humans")
    
class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humans = db.relationship("Human", secondary=dogs_table, back_populates="dogs")
```


```python

```
