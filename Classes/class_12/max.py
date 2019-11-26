# Exercise
# Create a function that receives a list of numbers and print
# the highest number in the list
# _____________________________
#< Don't use the max function! >
# -----------------------------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||

def listmax(l):
    actual_max = l[0]
    for number in l:
        if number > actual_max:
            actual_max = number
    return actual_max

print(listmax([12,15,1341,23412,461345,134,1234]))
