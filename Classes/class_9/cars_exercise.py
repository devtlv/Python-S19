cars = ['Toyota', 'Honda', 'Mazeratti', 'Honda','Ferrari', 'Audi', 'Seat', 'Peugeot']

# Print out which company wasn't duplicated
for car in cars:
    if cars.count(car) == 1:
        print("{} isn't duplicated in the list".format(car))

# Remove duplicates
cars_without_duplicates = []
for car in cars:
    if car not in cars_without_duplicates:
        cars_without_duplicates.append(car)

cars = cars_without_duplicates

# Count how many manufacturers are in the list
print("There are {} manufacturers in the list".format(len(cars)))

# Print manufacturers in descending order
print("Here are the cars manufacturers in descending order:")

for car in sorted(cars, reverse=True):
    print(car)

###########
# Create a counting variable
o_count = 0
not_i_count = 0
# Go through every car manufacturer
for car in cars:

    if 'o' in car.lower():
        o_count += 1

    if 'i' not in car.lower():
        not_i_count += 1


print("{} car manufacturers have an o in their names".format(o_count))
print("{} car manufacturers have no i in their names".format(not_i_count))

# Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name
for car in sorted(cars):
    # Manual way to do this
    reversed_car = ""
    for letter_index in range(len(car)-1, -1, -1):
        letter = car[letter_index]  # Retrieving letter at index
        reversed_car += letter

    # Lazy (right) way to do this
    reversed_car = car[::-1]
    print(reversed_car)










