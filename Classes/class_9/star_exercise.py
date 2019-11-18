# Using a for loop
# Draw this:
#*
#**
#***
#****
#*****
lines = input("How many stars do you want me to draw? ")
lines = int(lines)

for x in range(1, lines+1):
    print("*"*x)
