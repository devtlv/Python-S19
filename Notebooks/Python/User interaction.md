# User interaction 

A lot of ways exist in programming to get an input from the user, input fields, clicks, urls, etc.. 

In CLI (command line interfaces) python programs, we can pause the program for a certain time (until the user types something), then store his input into a variable and continue the program.

This can be done with the `input` function, this function is a bit particular, because it wait for the user to write something before continuing the program. This function can receive a message in argument, that will be displayed to the user.

Here is an example:
```python
age = input("How old are you? ")
print("You are {} years old".format(age))
```


This piece of code will do the following:
1) Display "How old are you to the user
2) Pause the program until the user to type something and hit `<Enter>`
3) Store the user's input into the `age` variable
4) Continue the program and print the message.


