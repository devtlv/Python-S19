import time
import random

my_functions = []
my_functions_dic = {}

def add_to_list(function):
    my_functions.append(function)
    return function

def add_to_dic(function_name):
    def decorator(function):
        my_functions_dic[function_name] = function
        return function
    return decorator

@add_to_dic("say hello")
def say_hello(name):
    print("Hello, {}, nice to meet you !".format(name))

@add_to_dic("ic")
def icecream(flavour):
    print("Here is a {} icecream".format(flavour))

@add_to_dic('/bark.html')
def bark():
    print("WOOF")

my_functions_dic['b']()
