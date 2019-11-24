# 
# Write a program that checks the validity of a password.
# 
# Ask the user for a password, and then make sure that the password follow those criterias:
# 
# - At least 1 lower case letter.
# - At least 1 number.
# - At least 1 upper case letter.
# - At least 1 character from [$#@].
# - Minimum length of password: 6.
# - Maximum length of password: 12.

def check_length(string):
    """
    This function receives a string and return True if
    the string's length is between 6 and 12 and False
    if it doesn't
    """
    if 6 < len(string) < 12:
        return True

    return False

def has_right_symbols(string):
    """
    This function receives a string and return True if
    the string contains at least one of the following
    symbols: "$#@" and False if it doesn't
    """
    for letter in string:
        if letter in "$#@":
            return True
    # End of the loop, we still didn't see any numbers, else we 
    # woud have exited the function
    return False

def has_upper_letter(string):
    """
    This function receives a string and return True if
    the string contains at least one upper letter and False
    if it doesn't
    """
    if string.islower():
        return False

    return True

def has_number(string):
    """
    This function receives a string and return True if
    the string contains at least one number and False
    if it doesn't
    """
    numbers = '0123456789'
    for letter in string:
        if letter in numbers:
            return True

    # End of the loop, we still didn't see any numbers, else we 
    # woud have exited the function
    return False


def has_lower_letter(string):
    """
    This function receives a string and return True if
    the string contains at least one lower letter and False
    if it doesn't
    """
    if string.isupper(): # This is checking if all the letters 
        return False     # in the string are upper cased

    return True

def check_password_validity(password):
    if has_lower_letter(password) and \
        has_number(password) and \
        has_upper_letter(password) and \
        has_right_symbols(password) and \
        check_length(password):
        return True

    return False

my_password = "aaAA1@#$3"
if check_password_validity(my_password):
    print("Good password !")
else:
    print("Wrong password !")












