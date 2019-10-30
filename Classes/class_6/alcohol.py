age = input("How old are you ? ")
country = input("Where do you live ? ") 
age = int(age)

if (country == "US" and age > 21) or (country != "US" and age > 18):
    print("You can buy alcohol")
else:
    print("Drink pepsi")

 # _____________
 #<  Second way! >
 # -------------
 #        \   ^__^
 #         \  (oo)\_______
 #            (__)\       )\/\
 #                ||----w |
 #                ||     ||

if country == "US":
    if age > 21:
        print("You can buy alcohol")
    else:
        print("Drink water")
else:
    if age > 18:
        print("You can buy alcohol")
    else:
        print("Drink water")
