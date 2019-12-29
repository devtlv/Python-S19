# Mid Exam



### Question 1

In your words, write a definition of all those words:

- Class
- Variable
- Function
- String
- List
- Dictionary
- For loop
- Boolean
- Decorator



### Question 2

What is the difference between an object and a class ?



### Question 3 

If you want to add one to every number in a list, will you do a for loop or a while loop ? Why ?



### Question 4

Without running it, what is the error in this program ? 

```python
def my_function(a, b):
    return a*2 + b*2

result = my_function()
```



### Question 5

Without running it, what is the problem in this program ? 

```python
def my_function(a, b):
    result = a*2 + b*2

result = my_function()
print(result)
```



### Question 6

Without running it, what is the error in this program:

```python
class Dog:
    def __init__(self, name, color):
        self.name = name
    	self.color = color
        
    def describe():
        print("My name is {} and I'm a {} dog".format(self.name, self.color))
        
dog = Dog()
dog.describe()
```



### Question 7

What does `import` means ? 



### Question 8

What is the purpose of this function:

```python
import time

def my_function(function):
    a = time.time()
    function()
    b = time.time()
    return b - a
```



### Question 9

Make a function that opens a file and prints his output



### Question 10 

Are `mylist1` and `mylist2` the same list ? Why ?

```python
mylist1 = ['a', 'b', 'c']
mylist2 = ['c', 'b', 'a']
```



### Question 11

Are `mydict1` and `mydict2` the same dictionary ? Why ?

```python
mydict1 = {'a':1, 'b':2, 'c':3}
mydict2 = {'c':3, 'b':2, 'a':1}
```



### Question 12

What does "inheritance" means ? Write an code example.



### Question 13

What is the problem in this code:

```python
def run_function(function):
    print("running", function.__name__)
    return function()

def myfunction():
    print("Hello world")
    
run_function(my_function())
```



### Question 14

What is the output of this program ?

```
a, b = ([1, 2, 3], [4, 5, 6])
print(a[:2])
print(b[2:])
```



### Question 15

How can you write a function that receives an indefine number of arguments ? Write an example



### Question 16

Rick Sanchez is a scientist, he likes building little robots. He got a lot of robots, and he stores them in his garage. His garage is ordered with places numbers, from 1 to infinite (it's a wide garage).

Create a class `RicksGarage` with two attributes `robots_places`, a dictionary that associates each little robot with his place number, and `robots_names`, another dictionary that associates the name of each robot to his place. `RicksGarage` also have two methods `add_robot` and `remove_robot`. 

Create another class `LittleRobot` with *at least* those attributes: `name` `place_number` and `purpose`  (you can add as many attributes as you want). Each time he creates a new robot, Rick places it in the next available place (which is the place of the last robot + 1). 

Those little robots classes should also have a method `run`, that is supposed to execute the main job of the robot.

Implement a method in the garage `use_robot` that receives a robot name and an undefined number of keyword arguments. This function retrieves the robot with this name and call his `run` method, sending the keyword arguments as parameters for the `run` method.

Create those robots:

- A robot that pass butter
- A robot that put every string in upper case
- A robot that return the sum of all the numbers in a list 
- A robot that yells at Jerry
- A robot that receives a string and a filename and write this string into the file.



### Question 17

Joe Goldberg is a young bookstore owner, he got a lot of old books. The problem is that those old books can be eaten by some weird insects, but thankfully, Joe is cleaning his bookstore every day.

One day, Joe left his bookstore to build a new life in Europa, no one is cleaning it anymore, so the insects are free to eat all the books there.

Here is how it goes: Each day, an insect eats a book, then make a baby, and each one go to eat another book. Basically, every infected book infects two other books the next day. The books are separated by categories, and the categories shelfs are too far one from another, thus when the insects are finished with one shelf, they just stay there and don't infect another one.

Create a class `Shelf` with two attributes `n_infected_books` `n_clean_books`, and a class `BookStore` with two attributes `alive_shelfs` and `dead_shelfs`, a list of `Shelf` objects. Each class should have a `next_day()` method that simulate what happen on the next day.

On the first day, there is one insect in each self (so `n_infected_books = 1`), and each day, every infected book infects two books. When every book of a shelf is infected, the shelf is considered as dead. When every shelfs are infected, the bookstore closes.

Implement a method `run()` in the `BookStore` class that run every day until the bookstore closes, and then print how many days it took. 

#### 