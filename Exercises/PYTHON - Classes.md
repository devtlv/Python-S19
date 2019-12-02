### Exercise 1 (easy)

Create a `Car` class.  
A `car` object need to have a color, a brand name and a maximal speed.  
Create a function that print an advertisement for this car.

### Exercise 2 (medium)

Create an `Hotel` class.  
`Hotel` objects need to have a name, a location, and a number of residents (on initialization, this number should be automatically set to 0).  
Create two functions `check_in` and `check_out` that will be ran when someone enters/leaves the hotel. Those functions should modify the number of current residents.  
If a person try to enter an hotel that is already full, tell him gently that you won't be able to host him.  

### Exercise 3 (hard)
Add a `current_fuel` and a `fuel_capacity` attribute to your `Car` class from exercise 1, and add a function `fuel_car`. Every liter of gas cost 2$, the `fuel_car` function should return the cost of the operation you just made (Bonus: You can also add a limit to the gas cost as an argument).  
Now add a `fuel_cost` attribute that represents the amount of gas your car need to spend to travel 1km, then add a `travel` function that receives a number of kilometers and simulate a travel.  
If the car runs out of gas then.. too bad for the user.



