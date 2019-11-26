# Functions

Functions are named blocks of code that are designed to do one specific job.

When you want to perform a particular task that you’ve defined in a function, you call the name of the function responsible for it.

If you need to perform that task multiple times throughout your program, you don’t need to type all the code for the same task again and again; you just call the function dedicated to handling that task, and the call tells Python to run the code inside the function.

Functions allow you to break your programs into small parts, each of which does one specific job. 

By using functions, you’ll be able to write more efficient code that’s easier to troubleshoot and maintain and that can be reused in many different programs.



#### Syntax

This is a simple function that says hello:

```python
def say_hello():
    """A function that says hello"""
	print("Hello!") 
    
say_hello()
```

This example shows the simplest structure of a function. 



**Definition** 

The first line uses the keyword `def` to inform Python that you’re defining a function. 

This is the function definition, which tells Python the *name* of the function. 

The parentheses hold some information about parameters, we'll see this very soon. In this case, the name of the function is `say_hello()`, and it needs no parameters, so its parentheses are empty (Even so, the parentheses are required.) 

Finally, the definition ends with a colon and all the code that is in included in the function needs to be *indented*.



**Code**

Any indented lines that follow `def say_hello():` make up the body of the function. 

The text on the second line is a comment called a *docstring*, which describes what the function does. *Docstrings* are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs. 

The line `print("Hello!")` is the only line of actual code in the body of this function, so `say_hello()` has just one job: print "Hello!".



**Function call**

When you want to use this function, you *call* it. A function *call* tells Python to execute the code in the function. To *call* a function, you write the name of the function, followed by any necessary parameters in parentheses, as shown on the last line. Because no information is needed here, calling our function is as simple as entering `say_hello()`. As expected, it prints `Hello!`.



#### Passing information to a function

Once powerful feature of functions is *arguments*, or *parameters*. They are values in the functions that can be changed each time we call it. For example, the `say_hello` function should say hello to someone, like "Hello Rick!", but because we want to be able to change this name (and print hello to "Morty" as well), we don't hard-code the name in the function. Instead of this we just use an *argument* for it.

```python
def say_hello(username):
    print("Hello "+username)

say_hello("Rick")
say_hello("Morty")
```

In the definition, we add the variable that will accept the value of the username, and then in the function call, we pass a value for it.

Here the function will execute the same code but with a different value for `username`.

**Be careful!:** If the function expects one argument, you can pass only one argument, less or more will throw an error.



Here is an example of a function that accept more than one argument:

```python
def say_hello(username, language):
    if language="EN":
        print("Hello "+username)
    elif language="FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)
        
say_hello("Rick", "FR")
```

This function accepts two arguments:

-  The first one, `username`, is used to store the value of the username that we need to greet.
- The second one, `language`, is used to store the language of the greeting.

When *calling* the function, we pass two arguments in the right order (first the `username` and then the `language`).

Arguments matched up this way (by order) are called *positional arguments.*



> **Careful:** You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments.
>
> If you get weird results, check to make sure the order of the arguments in your function call matches the order of the parameters in the function’s definition.



**Keyword arguments**

A *keyword argument* is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion. 

Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.

Let's rewrite the `say_hello` function call using *keyword arguments*. 

```python
def say_hello(username, language):
    if language="EN":
        print("Hello "+username)
    elif language="FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)
        
say_hello(username="Rick", language="FR")
```

> **Careful:** When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition

The function `say_hello` hasn’t changed. But when we call the function, we explicitly tell Python which parameter each argument should be matched with. 

When Python reads the function call, it knows to store the argument 'Rick' in the parameter username and the argument 'FR' in language. 



The order of keyword arguments doesn’t matter because Python knows where each value should go. The following two function calls are equivalent:

```
say_hello(username="Rick", language="FR")
say_hello(language="FR", username="Rick")
```



You can use both *keyword* and *positional* arguments in the same function call, but you need to place every *positional* argument before the *keyword* ones.

For example, this will work:

```python
say_hello("Rick", language="FR")
```

But this wont:

```python
say_hello(username="Rick", "FR")
```



**Default values**

When writing a function, you can define a default value for each parameter. 

If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value. 

So when you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call. 

Using default values can simplify your function calls and clarify the ways in which your functions are typically used. 

For example, if you notice that most of the calls to `say_hello()` are being used to prompt greetings in English, you can set the default value of `language` to "EN". Now anyone calling `say_hello` in English can omit that information:

```python
def say_hello(username, language="EN"):
    if language="EN":
        print("Hello "+username)
    elif language="FR":
        print("Bonjour "+username)
    else:
        print("This language is not supported: " + language)

say_hello("Rick")
# OR
say_hello(username="Rick")
```

We changed the definition of `say_hello` to include a default value, "EN", for `language`. 

Now when the function is called with no `language` specified, Python knows to use the value "EN" for this parameter.

To use a language other than english, you could use a function call like this:

```python
say_hello("Rick", "FR")
# OR
say_hello(username="Rick", language="FR")
```

Because an explicit argument for `language` is provided, Python will ignore the parameter’s default value.

> When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.



**Avoiding argument errors**

When you start to use functions, don’t be surprised if you encounter errors about unmatched arguments. Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work. 

For example, here’s what happens if we try to call `say_hello()` with no arguments:

```python
Traceback (most recent call last): 
    File "pets.py", line 6, in <module> say_hello()
TypeError: say_hello() missing 2 required positional arguments: 'username' and 'language'
```

The first line of the traceback tells us the location of the problem, allowing us to look back and see that something went wrong in our function call.

On the second one the offending function call is written out for us to see. 

Then on the third the traceback tells us the call is missing two arguments and reports the names of the missing arguments.

Python is helpful in that it reads the function’s code for us and tells us the names of the arguments we need to provide. This is another motivation for giving your variables and functions descriptive names. If you do, Python’s error messages will be more useful to you and anyone else who might use your code. 

If you provide too many arguments, you should get a similar traceback that can help you correctly match your function call to the function definition.



**Return values**

A function doesn’t always have to display its output directly. Instead, it can process some data and then return a value or set of values.

The value the function returns is called a return value. 

The return statement takes a value from inside a function and sends it back to the line that called the function. 

Return values allow you to move much of your program’s grunt work into functions, which can simplify the body of your program.



**Returning a simple value**

Let’s look at a function that takes a first and last name, and returns a neatly formatted full name:

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)
```

```
Jimi Hendrix
```

The definition of `get_formatted_name()` takes as parameters a first and last name. 

The function combines these two names, adds a space between them, and stores the result in `full_name`. 

The value of `full_name` is converted to `title` case, and then returned to the calling line. 

When you call a function that returns a value, you need to provide a variable where the return value can be stored. 

In this case, the returned value is stored in the variable `musician`. The output shows a neatly formatted name made up of the parts of a person’s name:



**Returning more than one value with a tuple**

We already saw that a tuple can be unpacked:

```python
my_tuple = ("jimi", "hendrix")
first_name, last_name = my_tuple
print("First name is: " + first_name)
print("Last name is: " + last_name)
```

```python
First name is jimi
Last name is hendrix
```



If so, we can return a tuple at the end of the function, and unpack it when we *call* it: 

```python
def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())

first, last = format_name("RICk", "mORTY")
print(first)
print(last)
```

```
Rick
Morty
```

The function receive a `first_name` and a `last_name`, then format them, and return them as a tuple.

On the function call, the tuple is unpacked into two variables, `first` and `last`.



**Passing list as function arguments**

Function arguments can be any python data type, you can pass strings as well as list.

For example, a function that greets a list of user:

```python
def greet_users(users):			 	# users should be a list
    for user in users:				# Because it's a list, we can loop through it
        print("Hello " + user.title() + " !") 		# For each user, print "hello" and then his name
        
usernames = ["steve", "stan", "debbie"]
greet_users(usernames)
```

```python
Hello Steve !
Hello Stan !
Hello Debbie !
```



### Seeing functions as address

When you run a program, your computer loads the source code from the hard disk (HDD) and start to allocate a piece of random access memory (RAM), which is a lot faster than HDD, but also smaller. RAM is used to store temporary values, like variables. 

A RAM card looks like this:

![Ram card](img/ram_pic.jpg)

All those chips are composed of sillicone transistors, which are basically binary switches, their value can be `0` or `1` they are called *bits*. Those switches are grouped by groups of 8, called *byte*s.

The amount of switches depends on the computer you're using, it's written somewhere on your system. When people are saying "My computer is leet, it got 16 GB RAM", most of the time they don't know what they talk about. It just mean that their computer contains 16 Gigabyte (16 billion) groups of 8 switches.

Each group has an address, and a value, here is what it looks like:

![transistors](img/ram_microscope.jpg)

Let's represent it as a table, for a 4GB RAM computer, the table will have 4 billion rows, each row is an "Address"-"Value" pair:

| Address | Value |
| ------- | ----- |
|         |       |

The processor is the only one who can fetch/modify a value in the RAM. The processor also have some groups of switches, called *registers*, those registers can store 32 or 64 bits, depending on your processor type. 

Now what happen when you run:

```python
my_name = "Eyal is a good teacher"
age = 5
```

The processor take each of those variables (`"Eyal"` and `5`), and try to store it in a registery.  Now the `5` can be stored in a registery, because 64 bits are enough to store `5`, but the text could never fit in it (Think that every letter is 8 bits..). The trick here is to store it somewhere in the RAM, and store the address of the first letter in the registry. This is called a *pointer*.

Here is the state of the RAM after this code has been ran:

| Address  | Value |
| -------- | ----- |
| 1        |       |
| ...      | ...   |
| 0xa2ef50 | 'E'   |
| 0xa2ef51 | 'y'   |
| ...      | ...   |
| 0xa2ef71 | a     |
| 0xa2ef72 | r     |
| 0xa2ef73 | \00   |

Now we can see a variable as a registery, because that's how the computer stores a value, here is now the state of the variables:

| Variable name | Variable value |
| ------------- | -------------- |
| age           | 5              |
| my_name       | *0xa2ef50      |

Here, `age` is 5, and `my_name` is a pointer to `0xa2ef50`.



Now for a function, what happen when you run:

```python
def my_function(name):
    name = name.title()
    print("Hello", name)
```

Actually the computer will put the code:

```python
name = name.title()
print("Hello", name)
```

somewhere into the memory, let's say at address `0x22efea`. And create a variable called `my_function`, which his value is `*0x22efea`. When adding round brackets `()` after `my_function`, it tells python to execute the code stored in `0x22efea`. 



Now that we know that functions are just addresses, we can use them in many other ways, as they were actual variables. For example, let's create three functions:

```python
def my_f1():
    print("Hello")
   
def my_f2():
    print("Word")
   
def my_f3():
    print("This is Rick!")
```

If we refer to functions as variables, we can store them in a list:

```python
list_of_functions = [my_f1, my_f2, my_f3]
```

> Be sure to remove the round brackets, else the function will be executed and you will store the result of it.

And now that we have a list of variables that can be executed when adding round brackets, let's execute them with a for loop

```python
for function in list_of_functions:
    print(function())
```



**Modifying a list in a function**

When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are permanent (even outside the function), allowing you to work efficiently even when you’re dealing with large amounts of data. 

For example, consider a company that creates 3D printed models of designs that users submit. Designs that need to be printed are stored in a list, and after being printed they’re moved to a separate list. The following code does this without using functions.

```python
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

# Simulate printing each design, until none are left. 
#  Move each design to completed_models after printing. 
while len(unprinted_designs) != 0:    
    current_design = unprinted_designs.pop() 
    
    # Simulate creating a 3D print from the design.    
    print("Printing model: " + current_design)    
    completed_models.append(current_design)    

# Display all completed models. 
print("\nThe following models have been printed:") 
for completed_model in completed_models:    
    print(completed_model)
```

```
Printing model: iphone case
Printing model: robot pendant
Printing model: dodecahedron

The following models have been printed:
iphone case
robot pendant
dodecahedron
```

This program starts with a list of designs that need to be printed and an empty list called `completed_models` that each design will be moved to after it has been printed. 

As long as designs remain in `unprinted_designs`, the while loop simulates printing each design by removing a design from the end of the list, storing it in `current_design`, and displaying a message that the current design is being printed. 

It then adds the design to the list of completed models. When the loop is finished running, a list of the designs that have been printed is displayed.



We can reorganize this code by writing two functions, each of which does one specific job. 

Most of the code won’t change; we’re just making it more efficient. 

The first function will handle printing the designs, and the second will summarize the prints that have been made:

```python
def print_models(unprinted_designs, completed_models):
    """    
    Simulate printing each design, until none are left.    
    Move each design to completed_models after printing.    
    """
    
    while unprinted_designs:        
        current_design = unprinted_designs.pop()            
        
        # Simulate creating a 3D print from the design.        
        print("Printing model: " + current_design)        
        completed_models.append(current_design)        

def show_completed_models(completed_models):    
    """
    Show all the models that were printed.
    """    
    print("\nThe following models have been printed:")   
    for completed_model in completed_models:        
        print(completed_model)        

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```



This program is easier to extend and maintain than the version without functions. 

If we need to print more designs later on, we can simply call `print_models()` again. 

If we realize the printing code needs to be modified, we can change the code once, and our changes will take place everywhere the function is called. 

This technique is more efficient than having to update code separately in several places in the program.



This example also demonstrates the idea that every function should have one specific job. 

The first function prints each design, and the second displays the completed models. 

This is more beneficial than using one function to do both jobs.

 If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions. 

Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.



> If you want to prevent a function from modifying a list, pass `my_list.copy()` instead of `my_list` in the arguments



### 