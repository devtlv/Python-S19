#!/usr/local/bin/python3
#
# debugging.py
# class_26

NAME = "Eyal"
AGE  = 21

def myfunction(l):
    print("Hello world")
    l.append(2)
    import ipdb; ipdb.set_trace()
    if len(l) == 5:
        return l
    else:
        return False

mylist = [1,2,3,4,5]
print(myfunction(mylist))
