# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
#
# - 1: Sort based on name
# - 2: Then sort based on age
# - 3: Then sort by score

user_input = input('Please input name, age and score in the following format: NAME, AGE, SCORE\n$ ')

name, age, score = user_input.split(', ')

print(name, age, score)
