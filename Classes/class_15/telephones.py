class Smartphone:

    def __init__(self, number, password, brand):
        self.number     = number
        self.password   = password
        self.brand      = brand

    def unlock_phone(self):
        user_pwd = input("Input password: ")
        if user_pwd == self.password:
            print("Phone unlocked !")
        else:
            print("Wrong password")


class Iphone(Smartphone):

    def __init__(self, number, password):
        super().__init__(self, number, password, 'Apple')

    def face_unlock(self):
        print("Phone unlocked!")

ameen_phone = Smartphone('05878493892', 'ilovepython', 'samsung')
eyal_phone  = Smartphone('0586878399', 'chocolat', 'oneplus')
anna_phone  = Iphone('58748239874', 'vanilla')
shauls_phone = Iphone('02824398235', 'shaul')




