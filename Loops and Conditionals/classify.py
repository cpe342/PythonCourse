from random import choice
food = choice(['apple','orange','bacon','steak','worm','dirt'])

if food == "apple" or food=="orange":
    print("Fruit")
elif food == "bacon" or food=="steak":
    print("Meat")
elif food == "worm" or food=="dirt":
    print("Yuck")
