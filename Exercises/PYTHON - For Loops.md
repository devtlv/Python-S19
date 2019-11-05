<!-- Tags=['ForLoop'] -->

### Exercise (easy)

Use a `for` loop to print the numbers from 1 to 20, inclusive.



### Exercise (easy)

Make a list of the numbers from one to one million, and then use a `for` loop to print the numbers. 

(If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)



### Exercise (easy)

Make a list of the numbers from one to one million, and then use `min()` and `max()` to make sure your list actually starts at one and ends at one million. Also, use the `sum()` function to see how quickly Python can add a million numbers . 



### Exercise (medium)

Make a list of the multiples of 3 from 3 to 30. Use a `for` loop to print the numbers in your list.



### Exercise (easy)

Write a program that returns the index of the first occurrence of an item in a list.



### Exercise (easy)

Write a little program that concatenate two lists together without using the `+` sign.



### Exercise (medium)

Write a program that insert an item at a defined index.



### Exercise (hard)

Write a program that put each word of a string in a list without using the `split` function.



### Exercise (hard)

Write a program that prints the longest word in a list.



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



### Exercise (medium)

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
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)
```


