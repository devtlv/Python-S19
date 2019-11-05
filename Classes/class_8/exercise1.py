### Exercise (medium)

#Count the number of spaces in a string.

s = "Hello world I love python !"

index = 0
spaces_count = 0

while index < len(s):
    letter = s[index]
    if letter == ' ':
        spaces_count += 1
    index += 1

print("There is {} spaces in this sentence".format(spaces_count))
