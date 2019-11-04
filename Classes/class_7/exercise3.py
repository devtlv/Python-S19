### Exercise 1 (easy)

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza .

pizza_toppings = [] # The list of all the toppings

user_topping = input('What would you like to put on your pizza?\n> ') # Topping asked by the user

while user_topping != 'quit':
    pizza_toppings.append(user_topping)
    user_topping = input("Would you like to put something else? (print 'quit' to exit)\n> ")

print("Thanks, your pizza contains:",pizza_toppings)
