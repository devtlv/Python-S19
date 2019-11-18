first_names = ['Mickey', 'Donald', 'Super']
last_names = ['Mouse', 'Duck', 'man']


# Hello Mickey Mouse
# Hello Donald Duck
# Hello Super man

# 1st method
index = 0
while index < len(first_names):
    print(first_names[index], last_names[index])
    index += 1

# 2nd method
for index in range(len(first_names)):
    print(first_names[index], last_names[index])

# 3rd method
for index, elem in enumerate(first_names):
    print(first_names[index], last_names[index])





