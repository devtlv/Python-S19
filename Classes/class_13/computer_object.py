class Computer():

    def __init__(self, computer_brand, color):
        print("A new computer has been created!")
        self.brand = computer_brand
        self.color = color

    def description(self):
        print('I am a {} {} computer'.format(self.color, self.brand))

computer_obj = Computer("Razer", "black")

computer_obj.description()
# This is translated to: Computer.description(computer_obj)

computer2 = Computer("Asus", "Black")
computer2.description()
