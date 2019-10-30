age = input("How old are you ? ")
age = int(age)

# _________________________________________
#/ Convert it to an int because the result \
#\ of input() is always a string.          /
# -----------------------------------------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||

if age > 18:
    print("You can buy alcohol")
else:
    print("Sorry, drink water")


