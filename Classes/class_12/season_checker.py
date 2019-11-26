#Exercise (medium)
#Ask to the user to insert a month (from 1 to 12)
#Display the season of the month inserted
#
#Spring runs from March (3) to May (5); Summer runs from June (6) to August (8); Autumn runs from September (9) to November (11); Winter runs from December (12) to February (2);

def month2season(month_nb):
    month_nb = int(month_nb)
    if 3 <= month_nb <= 5:
        return "March"
    elif 6 <= month_nb <= 8:
        return "Summer"
    elif 9 <= month_nb <= 11:
        return "Autumn"
    elif (month_nb == 12) or (1 <= month_nb <= 2):
        return "Winter"
    else:
        return False

while True:
    user_input = input("Please give me a month number, i'll tell you which season it is\n$ ")

    season = month2season(user_input)

    if season == False:
        print("Please input a month between 1 and 12")
    else:
        print("This month is in ", season)
        break




