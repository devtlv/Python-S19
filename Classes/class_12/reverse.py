def reverse_string(s):
    return s[::-1], len(s)

my_string = "Hello world"

reversed_string, length = reverse_string(my_string)

print(reversed_string)
print(length)

