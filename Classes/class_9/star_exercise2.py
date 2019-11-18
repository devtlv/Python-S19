# Draw this:
#      *
#     **
#    ***
#   ****
#  *****
max_stars = 5
for stars_nb in range(1,max_stars+1):
    print(" "*(max_stars-stars_nb) + "*"*stars_nb)

