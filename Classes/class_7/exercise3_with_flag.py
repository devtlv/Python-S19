### Exercise 1 (easy)

# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza .

pizza_toppings = [] # The list of all the toppings
quit_flag = False

while quit_flag == False:
    user_topping = input("Insert a topping: ")
    if user_topping == 'quit':
        quit_flag = True
    else:
        pizza_toppings.append(user_topping)

print("Thanks, your pizza contains:",pizza_toppings)
