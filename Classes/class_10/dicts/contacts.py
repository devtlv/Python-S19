

contacts = {"Eyal":"0586878399",
            "John":"0542815674",
            "Mario":"0512345678"}

contacts['Luigi'] = '05674883972'

for name, number in contacts.items():
    print('{}\t=>\t{}'.format(name, number))

seeked_name = "John"

if seeked_name in contacts:
    print("{} exists in the contacts".format(seeked_name))

seeked_nb = '0586878399'
for name, number in contacts.items():
    if number == seeked_nb:
        print(f"{number} is the number of {name}")
