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

### Exercise 4-4 (easy)
When a character is created, he should say something. Each class says a different thing, store this as a class attribute.  
When `Warrior` is created, he says `"Grrr.."`  
When `Sorcerer` is created, he says `"Wooba lubba dub dub !"`
When `Drood` is created, he says `"Hello World !"`

### Exercise 4-5 (hard)
Change this sentence class attribute to a list of sentence, each time a new character is created, he says the next sentence in the list, if there is no more sentences, just go back to the first one.

### Exercise 5 (medium)
Create a `Human` class.  
Create a family tree, a dictionary that stores members of a family, each member should be a `Human` object.

### Exercise 5-1 (medium)
Replace the family tree dictionnary by a `FamilyTree` class.  

### Exercise 6 (easy)
Create a `Player` class, the only attribute of a player for now is his name.  

### Exercise 7 (easy)
Create a `RockPaperScissors` game, the game is initialized with two `Player` objects, like this:  
```
rick = Player("Rick")
morty = Player("Morty")
game = RockPaperScissors(rick, morty)
```
Every player have a number of points, starting at 0.  

When `game.play()` is executed, the players play rock paper scissors, at the end, add 1 to the winner points.  

When `game.finish()` is executed, print the name of the winner and the score.  

### Exercise 8 (medium) 
Create a `TicTacToe` game, the game initialization receives two `Player` objects.  
```
rick = Player("Rick")
morty = Player("Morty")
game = TicTacToe(rick, morty)
```
The game should be run when `game.run()` is executed.  

To create a tictactoe game, you also need to create a `TicTacToeBoard` class, this board simulates a 3x3 grid. Use nested lists to do this:
```
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
```
This board class doesn't need any initialization parameters.  
Implement 3 functions: 
-  `add_symbol`, a function that **receives a symbol, an X coordinate and a Y coordinate** and draw this symbol at the X,Y place in the grid
-  `display`, a function that prints the rendered grid.
-  `is_finished`, a function that checks if the game is finished (if on player won or if the board is full)



### Exercise 9 (hard)
Create a **Cell Game**.  
A cell game is a game that simulate evolution, it's a 0 player game, it means that the game starts with an initial state, and run alone.  
The initial state is a grid (of any size) with some cells that can be dead or alive. For example:
```
_ _ _ _ *
_ * * _ *
_ * _ _ _
* * _ * _
* _ * * _

```
This is a 5x5 grid, every `_` is a dead cell, and every `*` is an alive one. When the game starts, it simulates generation, at each generation, the grid changes following these rules:
-  Any live cell with fewer than two live neighbors dies, as if caused by under population.
-  Any live cell with two or three live neighbors lives on to the next generation.
-  Any live cell with more than three live neighbors dies, as if by overpopulation.
-  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Create a program that simulate one generation, and then another that simulate n (a number given by the user) generations and print the output grid.

