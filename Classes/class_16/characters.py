class Character:

    def __init__(self,
                name,
                hair_color
                ):

        self.name       = name
        self.hair_color = hair_color
        self.lifepoints = 0

    def introduce(self):
        print("Hey, I'm {} haired {}".format(self.hair_color, self.name))

    def change_hair_color(self, new_hair_color):
        old = self.hair_color
        self.hair_color = new_hair_color
        print("{}'s hair changed from {} to {}".format(self.name, old, new_hair_color))

    def rest(self):
        self.lifepoints = 100

class Warrior(Character):

    first_scream = "GRRRR"

    def __init__(self, name, hair_color):
        super().__init__(name, hair_color)
        print(Warrior.first_scream)

    def roar(self):
        print("{} says: ROOAAAAR".format(self.name))

class Sorcerer(Character):

    first_scream = "Wubba Lubba dub dub !!"

    def __init__(self, name, hair_color):
        super().__init__(name, hair_color)
        print(Sorcerer.first_scream)

    def curse(self, name):
        print("{} Leviosa (this is a curse)".format(name))

class Drood(Character):

    first_scream = "Hello world !"

    def __init__(self, name, hair_color):
        super().__init__(name, hair_color)
        print(Drood.first_scream)

    def heal(self):
        self.lifepoints += 10
        if self.lifepoints > 100:
            self.lifepoints = 100

warrior = Warrior("Eyal", "Blue")
