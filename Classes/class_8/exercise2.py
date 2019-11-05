### Exercise (medium)

#Count the number of uppercase and lowercase letters in a string 

s = "Hello world I love PYTHON !"

index = 0
upper_count = 0
lower_count = 0

while index < len(s):
    letter = s[index]
    if letter.isupper():
        upper_count += 1
    elif letter.islower():
        lower_count += 1

    index += 1

print("There is {} upper cased letters and {} lower case letters in this sentence".format(upper_count, lower_count))
