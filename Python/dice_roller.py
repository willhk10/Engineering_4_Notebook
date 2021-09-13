import random

print("The Dice Roller of the Century")

def roll_dice():
	roll = random.randint(1,n)
	print("You rolled a %d "  % roll)

while True:
	val = input("Press enter to roll, or press x to quit")
	n = int(input("How many sides do you want on the die?"))
	r = int(input("How many dice do you want to roll?"))
	if val ==  "x":
		print("exiting")
		exit()
	else:
		for x in range (0,r):
			roll_dice()



