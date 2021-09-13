import random

def roll_dice():
	roll = random.randint(1,6)
	print("You rolled a %d "  % roll)

print("Automatic Dice Roller")
val = input("Press enter to roll, or press x to quit")
if val ==  "x":
	print("exiting")
	exit()
else:
	roll_dice()


