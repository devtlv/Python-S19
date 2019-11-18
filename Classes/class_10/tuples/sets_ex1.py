# Create a set called `my_fav_numbers` with your favorites numbers.
# Add two new numbers to it.
# Create a set called `friend_fav_numbers` with your friend's favorites numbers.
# Concatenate `my_fav_numbers` and `friend_fav_numbers` to `our_fav_numbers`.

my_fav_numbers = set([8,12])
friend_fav_numbers = set([1, 42, 57, 72])

our_fav_numbers = set()

#####
# 1st solution
for element in my_fav_numbers:
    our_fav_numbers.add(element)

for element in friend_fav_numbers:
    our_fav_numbers.add(element)

# 2nd solution
our_fav_numbers.update(my_fav_numbers)
our_fav_numbers.update(friend_fav_numbers)
#####


print(our_fav_numbers)
