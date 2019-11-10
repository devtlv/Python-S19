<!--Tags=['while loops']-->

# While Loops - 2

### Exercise 1 (easy)

Use a while loop to print every number from 5 to 100  

### Exercise 2 (easy)

What is the purpose of this program:
```python
user_input = input("> ")
while user_input != "p4ssw0rd":
    print("Access denied.")
    user_input = input("> ")
print("Access granted!")
```

### Exercise 3 (easy)

What is the problem in this program:

```python
user_input = input("Password: ")
while user_input != "my_password":
    print("Access denied")
print("Access granted")

```
And how can you fix it ?  


### Exercise 4 (medium)

You have two lists, `current_players` and `new_players`, use a while loop to transfer every player from `new_players` to `current_players`.

```python
current_players = ['Mario', 'Luigi', 'Peach']
new_players = ['Blue Toad', 'Red Toad', 'Green Toad']
```
At the end of your program, `print(current_players)` should be: 

```python
['Mario', 'Luigi', 'Peach', 'Blue Toad', 'Red Toad', 'Green Toad']
```
