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


### Exercise 4 (easy)
Create a class called `Character`, this is a parent class for all the characters of your game.
This class should have those attributes:
- `lifepoints`
- `name`
- `hair_color`  


And those functions:
- `introduce()`  
Display an introduction sentence on the character  
-  `change_hair_color()`  
Change the hair color of the character
-  `rest()`  
Set the lifepoints at 100

### Exercise 4-2 (medium)
Create three classes: `Warrior`, `Sorcerer` and `Drood`.  
They all are characters, but every one has a special attack:  
-  `Warrior` can `roar()`, when this function is called, the warrior screams loudly.
-  `Sorcerer` can `curse()`, when this function is called, he pronounce a scary curse against someone's name.
-  `Drood` can `heal()`, when this function is called, he restores 10 lifepoints to himself.

### Exercise 4-3 (hard)
The `Warrior` can now `attack()` another character, reducing his lifepoints by 10.  
The `Drood` can heal someone else, restoring him 10 lifepoints.
