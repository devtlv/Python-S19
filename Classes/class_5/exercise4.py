# Write a program that given a number X, calculate the result of X+XX+XXX+XXXX.
# For example, if X is 7, calculate 7+77+777+7777
#  ____________________________________
# / Don't use this:                    \
# \ x + x*11 + x*111 + x*1111          /
#  ------------------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||

x = 7

# Converting the number into text
x_as_txt = str(x)

# Processing the 3 other numbers
n1 = int(x_as_txt * 2)
n2 = int(x_as_txt * 3)
n3 = int(x_as_txt * 4)

# Calculating the result
result = x + n1 + n2 + n3

print("The result of {} + {} + {} + {} is: {}".format(x, n1, n2, n3, result))
