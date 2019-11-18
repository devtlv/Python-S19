### Exercise (easy)

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza .



### Exercise (easy)

A movie theater charges different ticket prices depending on a person’s age . If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15 .

 Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .


### Exercise (easy)

Given a list, use a while loop to print out every elements from the end to the beginning.

### Exercise (easy)
Without your computer, guess the output of this piece of code:
```python
i = 1
while True:    
    if i == 3: 
        break
    print(i) 
    i + = 1
```

### Exercise (easy)

Use a while loop to print every number from 5 to 100  

### Exercise (easy)

What is the purpose of this program:
```python
user_input = input("> ")
while user_input != "p4ssw0rd":
    print("Access denied.")
    user_input = input("> ")
print("Access granted!")
```

### Exercise (easy)

What is the problem in this program:

```python
user_input = input("Password: ")
while user_input != "my_password":
    print("Access denied")
print("Access granted")

```
And how can you fix it ?  


### Exercise (medium)

Take the last exercise, and apply it to a family, ask every member of the family their age, and at the end of the loop, tell them the cost of the tickets for the whole family.


### Exercise (medium)

Given a list, use a while loop to print out every element which his index is even.


### Exercise (medium)

A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.

Write a program that ask every user their age, and then tell them which can see the movie.

>  Try to add the allowed ones to a list. 


### Exercise (medium)

This time you have a list of users, and you want to remove every user that is below 16 years old.

Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.

At the end, print the final list.


### Exercise (medium)

Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.


### Exercise (medium)

Count the number of spaces in a string.


### Exercise (medium)

Count the number of words in a string.


### Exercise (medium)

Write a program that calculate the number of upper case letters and lower case letters in a string.

### Exercise (medium)

Without your computer, guess the output of this program:
```python
index = 0
my_list = [321, 312, 123, 434, 1235]
while index < len(my_list):
    s = str(my_list[index])
    print(s[-1])
    index += 1

```

### Exercise (medium)
What is the output of the following?¶
```python
    x = "abcdef"
    i = "a"
    while i in x:
        x = x[:-1]
        print(i, end = " ")
```

### Exercise (medium)

You have two lists, `current_players` and `new_players`, use a while loop to transfer every player from `new_players` to `current_players`.

```python
current_players = ['Mario', 'Luigi', 'Peach']
new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
```
At the end of your program, `print(current_players)` should be: 

```python
['Mario', 'Luigi', 'Peach', 'Blue Toad', 'Red Toad', 'Green Toad']
```

### Exercise (hard)

Convert a string into password format
Example:
input : `"mypassword"`
output: `"***********"`



### Exercise (hard)

Make a list called `sandwich_orders` and fill it with the names of various sandwiches . 

Then make an empty list called `finished_sandwiches`. Loop through the list of sandwich orders and print a message for each order, such as `I made your tuna sandwich`. 

As each sandwich is made, move it to the list of finished sandwiches. 

After all the sandwiches have been made, print a message listing each sandwich that was made. 



### Exercise (hard)

Using the list `sandwich_orders` from Exercise 8, make sure the sandwich 'pastrami' appears in the list at least three times.

Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a `while` loop to remove all occurrences of 'pastrami' from sandwich_orders. 

Make sure no pastrami sandwiches end up in finished_sandwiches.



### Exercise (hard)

Encrypt and decrypt a string with Caesar cipher. 

Check on internet to understand how Caesar cipher works.



### Exercise (hard)

Create a python mastermind, make a program that asks the user for a string, and then generate a sequence of random letters (the length of the sequence should be the same as the user's string) until he falls on the user's string. At each iteration, the program can compare his random string to the user's string, and keep the right letters.




