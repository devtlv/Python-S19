# You have a list of users, and you want to remove every user that is below 16 years old.
#
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
#
# At the end, print the final list. Example list:
#
names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
accepted = []

for person in names:
    age = input("{}, how old are you? ".format(person))
    if int(age) > 16:
        accepted.append(person)

print("The following ppl are accepted:", accepted)


