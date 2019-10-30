# Ask the user for a password, and then make sure that the password follow those criterias:

# - At least 1 lower case letter between.
# - At least 1 number.
# - At least 1 upper case letter.
# - At least one exclamation mark.
# - Minimum length of transaction password: 6.
# - Maximum length of transaction password: 12.

password = input("Please input your password: ")

check = 0

if password.isupper() == True:
    # This means that all the letters in password are uppercased letters
    print("Your password needs to contain at least one lowercased letter")
    check = 1

if password.isalpha() == True:
    print("Your password needs to contain at least one number")
    check = 1

if password.lower() == password:
    # This will check if the original password is equal to his lowercased version
    print("Your password needs to contain at least one uppercased letter")
    check = 1

if "!" not in password:
    print("your password needs to contain an exclamation mark")
    check = 1

if len(password) <= 6:
    print("Your password needs to have more than 6 characters")
    check = 1

if len(password) >= 12:
    print("Your password needs to have less than 12 characters")
    check = 1

if check == 0:
    print("Your password is OK")

