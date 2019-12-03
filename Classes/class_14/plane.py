class Plane():

    def __init__(self):

        self.places = {
            'A1': False,
            'A2': False,
            'B1': False,
            'B2': False,
        }

    def check_available_places(self):
        available_places = []
        for seat_name, is_taken in self.places.items():
            if is_taken == False:
                available_places.append(seat_name)
        return available_places

    def buy_ticket(self):
        # Print the available places
        available_places = self.check_available_places()
        if len(available_places) == 0:
            print("Sorry, the flight is full")
            return False

        print("Here are the availables places in our plane:")
        for place in available_places:
            print('-',place)

        # Get user input
        user_choice = input("Choose a seat: ").upper()

        # Check validity of user_input
        if user_choice not in available_places:
            print("Invalid input")
            return False

        # Simulate sell
        print("You just booked seat", user_choice)
        self.places[user_choice] = True



plane = Plane()




