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

    print("Your password is not between 6 and 12 characters")
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
    print("Your password needs to contain one of those symbols: $#@")
    return False

def has_upper_letter(string):
    """
    This function receives a string and return True if
    the string contains at least one upper letter and False
    if it doesn't
    """
    if string.islower():
        print("Your password doesn't contain any upper letter")
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
    print("Your password doesn't contain any number")
    return False


def has_lower_letter(string):
    """
    This function receives a string and return True if
    the string contains at least one lower letter and False
    if it doesn't
    """
    if string.isupper(): # This is checking if all the letters 
        print("Your password doesn't contain any lower letter")
        return False     # in the string are upper cased
    return True

def check_password_validity(password, validators):

    for validator in validators:
        result = validator(password)
        if result == False:
            return False

    return True

print("Welcome to The Password Checker")
print("Which validator would you like to add:")
print("1 - At least one lower letter")
print("2 - At least one upper letter")
print("3 - At least one number")
print("4 - At least one symbol")
print("5 - Length need to be between 6 and 12")
print("")
print("Type every number that you want to add, for example: 145")
user_choice = input("> ")

print("Now enter your password")
print("Don't worry.. we won't keep it (we will)")
user_pwd = input("> ")

functions_dict = {
    '1': has_lower_letter,
    '2': has_upper_letter,
    '3': has_number,
    '4': has_right_symbols,
    '5': check_length,
}

user_choices = list(user_choice)
validators = []
for number in user_choices:
    corresponding_function = functions_dict[number]
    validators.append(corresponding_function)

result = check_password_validity(user_pwd, validators)
if result:
    print("Your password match the criteria")
else:
    print("Your password doesn't match the criteria")









