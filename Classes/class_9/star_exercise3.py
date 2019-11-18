# Draw this:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *

max_stars = 10

for x in range(1, max_stars+1):
    print("*"*x)

for stars_nb in range(max_stars, 0, -1):
    print(" "*(max_stars-stars_nb) + "*"*stars_nb)

