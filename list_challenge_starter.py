
from random import *


#Level 1
firstName = ["Alexandra", "Lucy", "Megan", "Amy", "Anna", "Emily", "Cheva", "Selena"]
lastName = ["Smith", "Rietbrock", "Rose", "Barnard", "Weinstein", "Jed", "Malpass", "Doyle"]

x = randint(0, len(firstName)-1)
y = randint(0, len(lastName)-1)

print(firstName[x])
print(lastName[y])

#Level 2

starter = ["Bread", "Calamari", "Cesaer Salad", "Greek Salad", "Minestrone Soup"]
main = ["Mac & Cheese", "Lobster", "Grilled Chicek", "Vegetable Pasta", "Spaghetti and Meatballs", "Hamburger"]
dessert = ["Ice Cream", "Peach Tart", "Chocolate Cake", "Profiteroles", "Fruit Salad"]
sides = ["Brussel Sprouts", "French Fries", "Bacon", "Rice", "Asparagus"]

randomStarter = randint(0, len(starter)-1)
randomMain = randint(0, len(main)-1)
randomDessert = randint(0, len(dessert)-1)
randomSide = randint(0, len(sides)-1)

print(starter[randomStarter])
print(main[randomMain])
print(dessert[randomDessert])
print(sides[randomSide])

#Level 3
choice = True
while choice == True:
    fiveSyllable = ["An old silent pond", "splash! Silence again", "Autumn moonlight—", "into the chestnut", "In the twilight rain", "A lovely sunset", "I want to sleep","Softly, please", "Light of the moon", "Seems far away"]
    sevenSyllable = ["A frog jumps into the pond", "A worm digs silently", "These brilliant-hued hibiscus", "with sandals in my hand", "past the black winter trees", "It is yummy when it's hot", "I like to eat them daily"]

    random5 = randint(0, len(fiveSyllable)-1)
    random7 = randint(0, len(sevenSyllable)-1)
    random55 = randint(0, len(fiveSyllable)-1)

    if random5 != random55:
        print(fiveSyllable[random5])
        print(sevenSyllable[random7])
        print(fiveSyllable[random55])
        choice = False
