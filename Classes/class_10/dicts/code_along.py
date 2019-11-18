me_dict = {
    'first name': 'eyal',
    'last name': 'Shukrun',
    'age':2
}

me_dict['last name'] = 'Romero da crusas'

me_dict['eyes color'] = 'green'

del me_dict['last name']

for key, value in me_dict.items():
    print(key, value)

print(me_dict['first name'])
