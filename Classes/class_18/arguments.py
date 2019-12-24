def print_args(name,  *args, last_name="",**kwargs):
    print("My name is {} {}".format(name, last_name))
    for arg in args:
        print(arg)

    for k,v in kwargs.items():
        print(k, '-->', v)

def describe(name, lastname, age):
    print("Hey, i am", name, lastname)
    print("I am {} years old".format(age))

func_kwargs = {
    'name': 'Eyal',
    'lastname': 'Sanchez',
    'age':10
}

describe(**func_kwargs)
#describe(name="Eyal", lastname="Sanchez", age=10)



