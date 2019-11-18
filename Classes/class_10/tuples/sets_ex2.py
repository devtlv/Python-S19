random_list = [1,23,3151,314,234,235,62,23,24,52456,27]

random_list_as_set = set(random_list)

if len(random_list) == len(random_list_as_set):
    print("This list doesn't contain duplicates")
else:
    print("This list contains duplicates")

