class Animal:

    def __init__(self, name):
        self.name = name.upper()

    def eat(self):
        print(self.name, 'is eating')

    def sleep(self):
        print(self.name, 'is sleeping')

    def breath(self):
        print(self.name, 'is breathing')

    def __str__(self):
        return "{}".format(self.name)

class Eagle(Animal):

    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def hunt(self):
        print(self.name, 'is hunting')

eagle = Eagle('Richie', 'Yellow')



