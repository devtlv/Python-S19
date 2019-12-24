
def modify_function(f):
    def new_function():
        print("Im executing", f.__name__)
        f()

    return new_function

def myfunction2():
    print("Bye world")

### This is the
@modify_function
def myfunction():
    print("Hello world !")

### same as
def myfunction():
    print("Hello world !")
myfunction = modify_function(myfunction)

### This

import time

def timer_decorator(func):
    def new_function(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after  = time.time()
        print("Function {} took {} seconds to execute".format(func.__name__, after - before))

    return new_function

@timer_decorator
def one_to_million():
    s = 0
    for number in range(1000000):
        s += number
    print(number)

# Password decorator
mypassword = "chocolate"

def pwd_protect(func):
    def new_function(*args, **kwargs):
        pwd = input("This function is protected, give me your password: ")
        if pwd == mypassword:
            function_result = func(*args, **kwargs)
            print("Good password!")
            return function_result
        else:
            print("Wrong password")


    return new_function


@pwd_protect
def my_wall():
    return "Hello world im eyal"

@pwd_protect
def my_card_number():
    print("It's 000001")

def my_linkedin():
    print("Im a python teacher")

@pwd_protect
def my_bank_account():
    print("My password is: chocolate")

@pwd_protect
def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(5, 8)
    print(result)


