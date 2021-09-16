# Engineering_4_Notebook
### This is my exploration through Raspberry Pi, Python, and everything else Engineering 4 may offer.

## TableofContents
* [Hello World (First assignment with Pi)](#Hello_World)
* [Dice Roller](#Dice_Roller) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Spicy Version](#Spicy_Version_Of_Dice)*
* [Python Calculator](#Python_Calculator) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Spicy Version](#Spicy_Version)*
* 



# Hello_World
This [assignment](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/hello_world.py) required us to learn how to set up the Raspberry pi, which included logging into the Pi, using the Sudo Nano command to create the file, and running the file.
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Spicy_Dice_Roller.png" alt="alt text" width="600" height="500">
# Dice_Roller
The [dice roller](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/dice_roller.py) required us to import a library into the Raspberry pi library with 
``` python
import random
```
. This allowed me to create a dice roller that would select a random number 1 to 6. I then had to create a "while True:" loop that would go through the code infinitely. <br/>
There were very little challenges that I encountered throughout this assignment, with the only one being not having imported the "rand" function.

## Spicy_Version_Of_Dice
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Dice_Roller_Spicy.png" alt="alt text" width="600" height="400">
The spicy version was mostly identical to the original assignment, however one very important "else:" statement was added to the end, along with two more inputs.

``` python
else:
	for x in range (0,r):
		roll_dice()
```

The point of these lines were to roll the die as many times as were asked. An input to change the amount of die rolled was added and defined as "r", which was the ending range of the loop. Additionally, we had to make sure they could have as many faces on the die that they wanted. This was achieved by changing the static range of (1, 6) to (1, n), with n being an input of the amount of faces.

# Python_Calculator
~Description~

Here is the [Code](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/Python_Calculator.py) for this project.

## Spicy_Version
This was almost the exact same as the previous assignment, however with a small addition. I had to look up [how to code factorials](https://www.geeksforgeeks.org/factorial-in-python/) without using an imported math function. The code for this assignment is [HERE](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/python_calculator_spicy.py).


# [Back To Top](#Engineering_4_Notebook)
