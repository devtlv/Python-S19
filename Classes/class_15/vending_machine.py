class VendingMachine:

    def __init__(self):
        self.earnt_money = 0
        self.products    = []
        # self.products will be a list of dictionnaries that represent a product
        # name/price/quantity

    def stock_article(self, product_dict):
        # Check if the dictionnary is valid
        keys = ['name', 'price', 'quantity']
        for key in keys:
            if key not in product_dict.keys():
                print("Invalid product format")
                return False

        # Check if the article already exist --> update the quantity
        for ix, product in enumerate(self.products):
            if product['name'] == product_dict['name']:
                self.products[ix]['quantity'] += product_dict['quantity']
                return True

        self.products.append(product_dict)


    def buy_article(self, product_name):
        """
            This function gets the name of a product (str) and simulate the sell of this product.
            Returns True or False --> Success of the transaction
        """
        # Retrieve product dictionnary
        for ix, product_dict in enumerate(self.products):
            if product_dict['name'].lower() == product_name.lower():
                product_ix = ix

        # Check availability
        if self.products[product_ix]['quantity'] == 0:
            print("Sorry, this product isn't available.")
            return False

        # Display the price
        price = self.products[product_ix]['price']
        print("This product cost ${}".format(price))
        buyit = input("Do you want this {}?[Y/n]\n> ".format(product_name))
        if buyit.lower() == 'n':
            return False

        print("Enjoy your {} !!".format(product_name))
        # Sell it..
        self.products[product_ix]['quantity'] -= 1
        if self.products[product_ix]['quantity'] < 0:
            self.products[product_ix]['quantity'] = 0




machine1 = VendingMachine()

print("Hello and welcome to the Python Vending Machine")
print("What would you like to do:")
while True:

    print("1 - Buy an article")
    print("2 - Stock an article")
    print("Press x to exit")
    choice = input('> ')

    if choice == '1':
        print("Here is a list of the articles:")
        for product in machine1.products:
            print("{} - ${}".format(product['name'], product['price']))
        chosen_product = input("Which article would you like to buy?\n> ")
        machine1.buy_article(chosen_product)

    elif choice == '2':
        name = input("What's the name of the product you want to stock?\n> ")
        price = input("What's the price of the product you want to stock?\n> ")
        quantity = input("What's the quantity of the product you want to stock?\n> ")

        price = int(price)
        quantity = int(quantity)

        product_dict = {
                'name': name,
                'price': price,
                'quantity': quantity
        }
        machine1.stock_article(product_dict)

    elif choice == 'x':
        break

    else:
        print("Invalid choice")

    print("\n\n")








