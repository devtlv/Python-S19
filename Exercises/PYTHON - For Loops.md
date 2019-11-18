<!-- Tags=['ForLoop'] -->

### Exercise (easy)
Write a program that counts the number of element for a list, without the len function.
```python
    name=['Alex','Mike','Dylan','Yossi']
```

### Exercise (easy)
Write a program that print every name that starts by 'a'
```python
    name=['Alex','Mike','Dylan','yossi','Alan']
```

### Exercise (easy) 
Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.

### Exercise (easy)
You have a list of users, and you want to remove every user that is below 16 years old.

Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.

At the end, print the final list.

Example list:
```python
names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
```

### Exercise (easy)

Use a `for` loop to print the numbers from 1 to 20, inclusive.



### Exercise (easy)

Make a list of the numbers from one to one million, and then use a `for` loop to print the numbers. 

(If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)



### Exercise (easy)

Make a list of the numbers from one to one million, and then use `min()` and `max()` to make sure your list actually starts at one and ends at one million. Also, use the `sum()` function to see how quickly Python can add a million numbers . 


### Exercise (easy)

Write a program that returns the index of the first occurrence of an item in a list.



### Exercise (easy)

Write a little program that concatenate two lists together without using the `+` sign.

## Exercise (medium)
Create a board as following by using for loops:
```python
    X
    XX
    XXX
    XXXX
    XXXXX
    XXXXXX
    XXXXX
    XXXX
    XXX
    XX
    X
```



### Exercise (medium)

Make a list of the multiples of 3 from 3 to 30. Use a `for` loop to print the numbers in your list.


### Exercise (medium)

Write a program that insert an item at a defined index.


### Exercise (medium)

1. Here is a list of popular car manufacturers: https://pastebin.com/bkBRuvAZ 
2.  Paste it into your code, and store it in a variable. 
3. Convert it into a list using Python (don’t do it by hand!) 
4. Print out a message saying how many manufacturers/companies are in the list 
5.  Print the list of manufacturers in reverse/descending order (Z-A) 
6. Using loops or list comprehension: 
   1. Find out how many manufacturers’ names have the letter ‘o’ in them. 
   2. Find out how many manufacturers’ names do not have the letter ‘i’ in them 
   3. Print the above information out with meaningful output messages. 
7. (Bonus: There are a few duplicates in the list: 
   1. Remove these programmatically. (Hint: you can use sets to help you) 
   2. Print out the companies without duplicates, in a comma-separated list with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, ...”), and also print out a message saying how many companies are now in the list). 
8. (Bonus: print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name)


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


### Exercise (medium)

Draw the following pattern using for loops:

```text
    *
   **
  ***
 ****
*****
```


### Exercise (medium)
```python
What is the output of the following?¶
    x = ['ab', 'cd']
    for i in x:
        i.upper()
    print(x)
```

### Exercise (medium)
What is the output of the following?¶
```python
    x = ['ab', 'cd']
    for i in x:
        x.append(i.upper())
    print(x)
```


### Exercise (hard)

Given a list of integers and strings, put all the integers in one list, and all the strings in another one.



### Exercise (easy)

Draw the following pattern using for loops:

```text
*
**
***
****
*****
```


### Exercise (hard)

Draw the following pattern using for loops:

```text
*
**
***
****
*****
*****
 ****
  ***
   **
    *
```



### Exercise (hard)

Draw the following pattern using for loops:

```
      *
     ***
    *****
```

### Exercise (hard)

Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

```python
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if my_list[j] < my_list[minimum]:
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
```

### Exercise (hard)

Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

```python
my_list = [2, 13, 34, 23, 12, 111]
for fillslot in range(len(arr)-1,0,-1):
    max_pos = 0
    for location in range(1, fillslot+1):
        if arr[location] > arr[max_pos]:
            max_pos = location
    tmp = arr[fillslot]
    arr[fillslot] = arr[max_pos]
    arr[max_pos] = tmp
```

### Exercise (hard)

Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

```python
my_str = "I do"
my_text = "What I can't build, I do not understand."
found   = False
index = 0
for letter in my_text:
    if letter == my_str[index]:
        index += 1
        if index == len(my_str):
            found = True
            break
    else:
        index = 0

if found:
    print("<{}> was found in the text !".format(my_str))
else:
    print("<{}> is not in the text".format(my_str))
```

### Exercise (hard)

Execute this program manually (without the help of your computer), write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

### Exercise (hard)

Write a program that put each word of a string in a list without using the `split` function.



### Exercise (hard)

Write a program that prints the longest word in a list.

### Exercise (hard)


