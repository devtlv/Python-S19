class Human():

    def __init__(self, name, age, kindness, generosity, eyes_color):
        self.name       = name.title()
        self.age        = age
        self.kindness   = kindness
        self.generosity = generosity
        self.eyes_color = eyes_color

    def introduce(self):
        print("Hello, I'm", self.name)
        print("I am {} years old".format(self.age))
        print("My eyes are", self.eyes_color)

    def birthday(self):
        print("Happy birthday {} !".format(self.name))
        self.age += 1
        print("You are now", self.age)

eyal = Human('eyal', 20, 10, 10, 'green')
eyal.introduce()

eyal.birthday()
eyal.introduce()

