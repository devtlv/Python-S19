### Exercise (easy)

[Write](Write) a function called `display_message()` that prints one sentence telling everyone what you are learning about in this chapter. 

Call the function, and make sure the message displays correctly.



### Exercise (easy)

Write a function called `favorite_book()` that accepts one parameter, `title`. 

The function should print a message, such as "One of my favorite books is Alice in Wonderland".

Call the function, making sure to include a book title as an argument in the function call.



### Exercise (easy)

Write a function called `make_shirt()` that accepts a size and the text of a message that should be printed on the shirt.

The function should print a sentence summarizing the size of the shirt and the message printed on it. 

Call the function once using positional arguments to make a shirt. 

Call the function a second time using keyword arguments.

### Exercise (easy)

Make a list of magician’s names. 

Pass the list to a function called `show_magicians()`, which prints the name of each magician in the list.



### Exercise (easy)

Start with a copy of your program from Ex 6. 

Write a function called `make_great()` that modifies the list of magicians by adding the phrase `"the Great"` to each magician’s name. 

Call `show_magicians()` to see that the list has actually been modified.



### Exercise (medium)

1. Retirement age in Israel is 67 for men, and 62 for women (born after April, 1947). 

2. Create a function ‘get_age’. 
   1. It should have three integer parameters: year, month, and day. 
   2. Hard-code the current year and month in your code (there are better ways of doing this, but for now this will suffice.) 
   3. After calculating the age, the function should return the age as an integer.
   
3. Create a function ‘can_retire’. 
   1. It should take 2 arguments: sex and date_of_birth. 
   2. It should call your get_age function (with what arguments?) and receive an age back. 
   3. Now it has all the information it needs in order to determine if the person with the given sex and date of birth is able to retire or not. 
   4. Calculate. You may need to do a little more hard-coding here. 
   5. Return True if the person can retire, and False if he/she can’t. 
   
4. Ask for the user’s sex as “m” or “f”. 

5. Ask for the user’s date of birth in the form “yyyy/mm/dd”, eg. “1993/09/21”. 

6. Call can_retire to get a definite value for whether the person can or can’t retire. 

7. Display a message to the user informing them whether they can retire or not.

8. As always, test your code to ensure it works.

   

### Exercise (medium)

Modify the `make_shirt()` function so that shirts are large by default with a message that reads I love Python. 

Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message. 



### Exercise (medium)

Write a function called `describe_city()` that accepts the name of a city and its country. 

The function should print a simple sentence, such as "Reykjavik is in Iceland". 

Give the parameter for the country a default value. 

Call your function for three different cities, at least one of which is not in the default country.



### Exercise (medium)

Start with your work from Ex7. 

Call the function `make_great()` with a copy of the list of magicians’ names. 

Because the original list will be unchanged, return the new list and store it in a separate list.

Call `show_magicians()` with each list to show that you have one list of the original names and one list with `"the Great"` added to each magician’s name.



### Exercise (medium)

Write a function called `get_full_name()` that receives three arguments: a `first_name`, a `middle_name` and a `last_name`. But the `middle_name` should be optional, if it's omitted by the user, the name returned will only contain the first and the last name.

For example, `get_full_name(first_name="john", middle_name="hooker", last_name="lee")` will return `John Hooker Lee`. But `get_full_name(first_name="bruce", last_name="lee")` will return `Bruce Lee`.



### Exercise (medium)

Write a function that receives a list of numbers and return the highest number in the list and its position. 

Don't use any built in function.



### Exercise (medium)

Write a function that receive a string in argument and returns if all the characters are uppercase or not.



### Exercise (hard)

Write a function that implements ceasar cypher, it receives a string and a number `n` as argument, and then shifts all the letters of the string by `n` places, and returns the encrypted string.



### Exercise (hard)

Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
For example the list ["Hello", "World", "in", "reallylongword", "a", "frame"] will result as:

```
******************
* Hello          *
* World          *
* in             *
* reallylongword *
* a              *
* frame          *
******************
```



### Exercise (hard)

Execute that code manually (without using your computer) and find the output.
What is the purpose of it ?

```python
def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)
```



### Exercise (hard)

Write a function that converts English text to Morse code and another one that does the opposite.

Check on internet for translation table, every letter is separated with a space and every word is separated with a slash `/`. 


  
