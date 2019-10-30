# Loops

In computer programming, a *loop* is a sequence of instructions that is continually repeated until a certain condition is reached. 

Typically, a certain process is done, such as getting an item of data and changing it, and then some condition is checked such as whether a counter has reached a prescribed number. 

If it hasn't, the next instruction in the sequence is an instruction to return to the first instruction in the sequence and repeat the sequence. 

If the condition has been reached, the next instruction "falls through" to the next sequential instruction or branches outside the loop. 

A loop is a fundamental programming idea that is commonly used in writing programs.



#### While loop

 The `while` loop runs as long as (or while) a certain condition is true.

It will execute all the instructions in the loop, then test the condition, if the condition is still true, it will execute the loop again, and again, until the condition become false.



You can use a while loop to count up through a series of numbers. For example, the following while loop counts from 1 to 5:

```python
current_number = 1 
while current_number <= 5:    
    print(current_number)   
    current_number += 1
```

```
1
2
3
4
5
```

In the first line, we start counting from 1 by setting the value of `current_number` to `1`. 

The while loop is then set to keep running as long as the value of current_number is less than or equal to `5`. 

The code inside the loop prints the value of `current_number` and then adds `1` to that value with `current_number += 1`. (The `+=` operator is shorthand for `current_number = current_number + 1`.) 

Python repeats the loop as long as the condition `current_number <= 5` is `True`. Because `1` is less than `5`, Python prints `1` and then adds `1`, making the `current_number` 2. Because `2` is less than `5`, Python prints `2` and adds `1` again, making the `current_number` 3, and so on. 

Once the value of `current_number` is greater than `5`, the loop stops running and the program ends.



#### Infinite loop

Some conditions will always be `True`, for example, if we run this code:

```python
while 1 == 1:
    print("Looping...")
```

It will never stop, because 1 is always equal to 1. We can also use `while 1:` or `while True:`.



#### Using a flag

What about more complicated programs in which many different events could cause the program to stop running? 

For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active. This variable, called a *flag*, acts as a signal to the program. 

We can write our programs so they run while the flag is set to `True` and stop running when any of several events sets the value of the flag to `False`. As a result, our overall `while` statement needs to check only one condition: whether or not the `flag` is currently `True`. 

Then, all our other tests (to see if an event has occurred that should set the`flag` to `False`) can be neatly organized in the rest of the program.

For example: 

```python
active = True
while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' to when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'let me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")
```



#### Break and Continue

`break` and `continue` are two statements that helps us manage the loop flow.



**break:**

`break` exit the while loop immediately without running any remaining code in the loop, regardless of the results of any conditional.

For example, consider a program that asks the user about places they’ve visited. 

We can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:

```python
while True: 
    city = input("Please enter the name of a city you have visited (enter 'quit' to when you are finished): ")
    if city == 'quit':
        break
    else:
        print("I'd love to go to", city)

print("Goodbye !")
```

A loop that starts with `while True` will run forever unless it reaches a break statement. 

The loop in this program continues asking the user to enter the names of cities they’ve been to until they enter 'quit'.

When they enter 'quit', the break statement runs, causing Python to exit the loop:

```python
Please enter the name of a city you have visited: (Enter 'quit' when you are finished.) New York 
I'd love to go to New York! 

Please enter the name of a city you have visited: (Enter 'quit' when you are finished.) San Francisco 
I'd love to go to San Francisco! 

Please enter the name of a city you have visited: (Enter 'quit' when you are finished.) quit
```



**continue:**

Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop. 

For example, consider a loop that counts from 1 to 10 but prints only the numbers that aren't between 3 and 7:

```python
current_number = 0
while current_number <= 10:
    current_number += 1
    if 3 < current_number < 7: # If the number is between 3 and 7 
        continue 				# Go back to the beginning of the loop
        
```

```python
1
2
3
7
8
9
10
```



#### While loops and lists

**Display list elements**

We can use while loops to iterate over a list elements, by iterating over his indexes. Remember that you can use `len()` to get the length of a list.

Accessing a list element with his index can be done by printing `my_list[my_index]`, if we repeat this instruction while `my_index` is going from 0 to the length of the list, we will print every element of the list.

For example:

```python
my_index = 0
my_list = ['Hello', 'World', 'I am', 'Rick']

while my_index <= len(my_list):
    print(my_list[my_index])
```



**Add elements to a list**

We can also use the `append()` function to add an element to the list, let's try to write a program that ask for a user in which city he already been, and each time add this city to a list. Then tell him in how many cities he was.

```python
cities = [] 	# Define a list
while True: 	# Loop indefinitely
    # Ask the user for a city
    city = input("Please enter the name of a city you have visited: (Enter 'quit' when you are finished.): ")	
    
    if city == 'quit': 		# Test if the user input isn't "quit"
        break
    
    cities.append(city)		# Append the user city to the list

hm_cities = len(cities)
print("You were in {} cities".format(hm_cities))
```


