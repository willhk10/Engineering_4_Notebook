# ***Engineering_4_Notebook***
### This is my exploration through Raspberry Pi, Python, and everything else Engineering 4 may offer.

## Table_of_Contents
* [Hello World (First assignment with Pi)](#Hello_World)
* [Dice Roller](#Dice_Roller) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Spicy Version](#Spicy_Version_Of_Dice)*
* [Python Calculator](#Python_Calculator) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Spicy Version](#Spicy_Version)*
* [Quadratic Solver](#Quadratic_Solver)



# ***Hello_World***
This [assignment](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/hello_world.py) required us to learn how to set up the Raspberry pi, which included connecting and logging into the Pi, which was surpisingly more difficult than I had previously anticipated. There were 4 plugs from the USB that we had to connect to the pi, and it looked something like this. <br/>
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Pi.jpg" alt="alt text" width="500" height="500">

We then had to log in using the default **username:** *pi*, and **password:** *raspberry* using the Sudo Nano command to create the file, and we then ran the file.<br/>

<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Spicy_Dice_Roller.png" alt="alt text" width="600" height="500">
<br/>

# ***Dice_Roller***
The purpose of the [dice roller](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/dice_roller.py) was pretty self explanatory. We had to make a virtual dice with 6 sides. In order to do this, we had to figure out how to make things random, which required us to import a library into the Raspberry pi library with 
``` python
import random
```
This allowed me to create a dice roller that would select a random number 1 to 6. I then had to create a "while True:" loop that would go through the code infinitely. <br/>
There were very little challenges that I encountered throughout this assignment, with the only one being not having imported the "rand" function.
<br/>

## **Spicy_Version_Of_Dice**
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Dice_Roller_Spicy.png" alt="alt text" width="600" height="400">
The spicy version was mostly identical to the original assignment, however one very important "else:" statement was added to the end, along with two more inputs.

``` python
else:
	for x in range (0,r):
		roll_dice()
```

The point of these lines were to roll the die as many times as were asked. An input to change the amount of die rolled was added and defined as "r", which was the ending range of the loop. Additionally, we had to make sure they could have as many faces on the die that they wanted. This was achieved by changing the static range of (1, 6) to (1, n), with n being an input of the amount of faces.
<br/>

# ***Python_Calculator***
The [Python Calculator](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/Python_Calculator.py) was one of the more challening projects initially, as I had to review my knowledge of lists, and functions. The main purpose of the assingment was to have two numbers inputted, and for the calculator to spit out the sum, difference, quotient, product, and percentage(modulo). In order to set this up, I had to first use two input statements to have the two numbers I would be using for the calculations. Then, the function had to be defined and created. 
``` python
def doMath(a, b, operation): #SETS UP THE FUNCTION TO CALL IN THE CALCULATOR
    if operation == 1: # DEFINES SUM
        return int(a + b)
    if operation == 2: #DEFINES DIFFERENCE
        return int(a - b)
    if operation == 3: #DEFINES PRODUCT
        return int(a * b)
    if operation == 4: #DEFINES PRODUCT
        return int(a / b)
    if operation == 5: #DEFINES MODULO
        return int(a % b)
```
I could then use the definition of each operation as a numerical value to call it in a print statement. This looked something like this:
``` python
print("Sum:\t\t" + str(doMath(a,b,1)))  # a = first value
print("Difference:\t" + str(doMath(a,b,2))) # b = second value
print("Product:\t" + str(doMath(a,b,3))) # numerical value at the end calls the corresponding operation defined in the doMath function
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
```

## **Spicy_Version**
This was almost the exact same as the previous assignment, however with a small addition. We had to add another calculation - **the factorial**. I had to look up [how to code factorials](https://www.geeksforgeeks.org/factorial-in-python/) without using an imported math function. The only addition I had to make to the code were some lines defining factorials:
``` python
if operation == 6: #DEFINES FACTORIAL
        babba = 1
        for i in range(1,a+1):
           babba = a * babba
        return(babba)
    if operation == 7: #DEFINES FACTORIAL
        boey = 1
        for i in range(1,b+1):
           boey = a * boey
        return(boey)
```
Since a factorial is essentially raising a number to its own value, the code above runs through a loop ***a*** (value to find factorial of) times, and multiplies the previous value by ***a*** each time. 
<br/>

# ***Quadratic_Solver***


# [Back To Top](#Engineering_4_Notebook)
