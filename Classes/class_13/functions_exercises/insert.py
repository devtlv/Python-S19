def insert(lst, index, elem):
    new_list = []
    for count, e in enumerate(lst):
        if count == index:
            new_list.append(elem)
        new_list.append(e)

    return new_list

# ______________________________
#< You can also do it this way! >
# ------------------------------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||
#
def insert(lst, index, elem):
    return lst[:index] + [elem] + lst[index:]

