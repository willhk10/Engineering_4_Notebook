# ***Engineering_4_Notebook***
### This is my exploration through Raspberry Pi, Python, CAD, and everything else Engineering 4 may offer.

### Useful links - 
[MP4 to .Gif](https://cloudconvert.com/mp4-to-gif)


## Table_of_Contents
* [Hello World (First assignment with Pi)](#Hello_World)
* [Dice Roller](#Dice_Roller) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Spicy Version](#Spicy_Version_Of_Dice)*
* [Python Calculator](#Python_Calculator) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Spicy Version](#Spicy_Version)*
* [Quadratic Solver](#Quadratic_Solver)
* [Separating Words for Some Reason](#LoopsAndStrings) <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *[Making It Harder for Some Reason](#LoopsAndStrings_Spicy_Version)*
* [Hackman (Hangman, but you cut him apart) ](#Hangman)
* [Sudoku!!!!!](#Sudoku)
* [Skateboard!](#Skateboard_CAD)
* [Legos!](#Legos)
* [Multi Tool](#multi-tool)
* [Pi LED Blink](#pi-led-blink)
* [Shutdown Button](#shutdown-button)
* [GPIO Pins - I2C](##gpio-pins---i2c)
* [Headless Accelerometer](##headless-accelerometer)
* [Camera](#camera)

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>


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
#### [Back To Top](#Engineering_4_Notebook)

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
#### [Back To Top](#Engineering_4_Notebook)

<br/>

# ***Quadratic_Solver***
The [Quadratic Solver](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/Quadratic_Solvey.py) is a program that solves a quadratic equation for the two roots, and if there are no real roots, does not create an error but rather exits the program. The program i created accepts three values: The first being the coefficient of a^2, the second being that of bx, and the last being the constant of the equation. <br/>
### *Process*
I knew that I would need to use the quadratic equation, which is (-b +- sqr(b^2 -4ac))/2 , so all I had to do was ask for the values of a, b, and c, and just stick it into the equation. Right? <br/>
***no.*** <br/>
I had to first create a function called doMath, and solve for the discriminant of the equation and determine if it was positive or negative with this line:
```python
discrim = int((b*b)- 4 * a * c)
```
We could then either solve for the roots if it was positive, or exit the program if it was negative:
```python
if discrim >= 0:
        root1 = int(-b + sqrt((b*b)- 4 * a * c))/ (2* a)
        root2 = int(-b - sqrt((b*b)- 4 * a * c))/ (2* a)
        discrim = int((b*b)- 4 * a * c)
        roots = [root1, root2]
        return roots, discrim 
    if discrim < 0:
        return "", discrim
```
Since Mr. Miller decided to be difficult and not allow us to print everything out in the function itself, we had to learn how to call lines and variables outside of the function itself. That is where these two lines come into play:
```python
        roots = [root1, root2]
        return roots, discrim 
```
Because this is all inside of the function doMath, I then had to actually call the function, while defining the variables beforehand as to not get any error messages. Mr. Miller and I struggled with this for some time. Here is the final result of the printing function that you see after inputting the three variables.
```python
(roots, discrim) = doMath(a, b, c)
    if discrim >= 0:
        print("root 1: " + str(roots[0]))
        print("root 2: " + str(roots[1]))
    else:
        print("No Real Roots")
```
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/quadraticsolver.png" alt="alt text" width="1080" height="720">
<br/>

# ***LoopsAndStrings***
The purpose of this [assignment](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/StringsAndLoops.py) was to learn how to use the .split function, as well as exploring more about arrays, lists, and loops. We had to receive a sentence in an input and then seperate it into letters with a line break inbetween each one, and then add a dash in between every space in the sentence, with an extra dash at the end. <br/>
I first had to do a brief review of how to write [incrementing loops,](https://www.geeksforgeeks.org/ways-to-increment-iterator-from-inside-the-for-loop-in-python/) strings, and use the [.split](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_split2) function. 
```python
for i in split1:
    print("-")
    for b in i:
        print(b)
print("-")
```
These lines of code are going through each line of the list provided by the split input and printing out each character on a line. The print("-") is inputting a dash whenever there is a gap inbetween words. <br/>

### *LoopsAndStrings_Spicy_Version*
The purpose of this assignment is to do the code for the Loops and Strings assignment in as little amount of lines as possible. I successfully got the code from 9 lines all the way down to 5. I do have to give some credit to my classmate [Alden Dent](https://github.com/adent11) for assisting me with getting it to 1.
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/stringsandloops.png" alt="alt text" width="1080" height="720">


# ***Hangman***
Before the explanation, here are a few things you should look up and understand before you attempt to write the [Hangman program](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/PerfectHangman.py) You need to understand how to take the length of a word and use it in code, use functions, and return variables inside of a function. [Here](https://www.w3schools.com/python/python_functions.asp) is a really good resource that I was fortunate enough to find for help with functions.
<br/>
I did not separate the inital assignment from the spicy version, so this project is essentially the proper way to create a Hangman game. The **goal of the assignment** is to create a working hangman game that prints out the hangman whenever a guess is incorrect, as well as storing and printing out all past incorrect guesses. If a guess is correct, it slots the correct guess into the corresponding location in the dashes. The program additionally does not let you make any duplicate guesses, right or wrong, or print out more than one letter.
The code starts out with defining the body of the hangman - 
```python
err1 = "---??? \n   O \n  \|/ \n   | \n  /  "
err2 = "---??? \n   O \n  \|/ \n   | \n   "
err3 = "---??? \n   O \n  \|/ \n    "
err4 = "---??? \n   O \n  \| "
err5 = "---??? \n   O \n  \ "
err6 = "---??? \n   O \n   "
err7 = "You killed him!"
```
Since there are only 7 parts of the body that we print, you only get 7 errors.
<br/>
We then make our first function, which prints out the proper string of hangman pieces for the amount of errors:
``` python
def errors(a):
    if a == 1:
        print(err1)
    if a == 2:
        print(err2)
    if a == 3:
        print(err3)
    if a == 4:
        print(err4)
    if a == 5:
        print(err5)
    if a == 6:
        print(err6)
    if a == 7:
        print(err7)
```
The most difficult part of the code was the function to show the guesses and store them through every guess
``` python
blanks = "_" * len(word)
def showguesses(b, Correctguesses, blanks):
    #Correctguesses = ["a","m","e"]
    for Correctguesses in word: #repeat the amount of time that the guesses are in the word
        if Correctguesses == word[b]: #if the guess is the same as the current letter being checked in the original word, do the following code
            blanks = blanks[:b] + word[b] + blanks[b + 1:] #changing the blank line to the correct guess
    return blanks
```
this works by repeating through an if statement the amount of times that a correct guess is in the word given by the user. "Blanks" is initially a word with equal length to the word to guess, but it is all underlines. The code counts through each value in the word to determine where the guess is in the initial word, and then places the guess in the according location in the blanks string.
<br/>
**Reflection** - Looking back on this assignment, I realized that I really had to do a lot of investigating into how to save the correct guesses, and not have it reset every time there is a correct guess. I did this by returning blanks at the end of the showguesses function.
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Hangman.png" alt="alt text" width="1080" height="720">

### TLDR; 
Look up how to use functions as well as when to return them inside the function, *len()* and *for* and *if* statements, and how to use logic in Python. 

---

# ***Sudoku***
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/bumpyride.gif" alt="alt text" width="500" height="200">


Let me preface this by saying that this assignment was a large challenge in so so many ways. Before attempting this assignment, you must understand a few things:
* [RECURSION](https://realpython.com/python-thinking-recursively/#:~:text=Recursive%20Functions%20in%20Python,-Now%20that%20we&text=A%20recursive%20function%20is%20a,met%20to%20return%20a%20result.) 
* [Logic](https://www.geeksforgeeks.org/python-logical-operators-with-examples-improvement-needed/)
* [Arrays](https://www.w3schools.com/python/python_arrays.asp)
* [Lists](https://www.w3schools.com/python/python_lists.asp)
* [Functions](https://www.w3schools.com/python/python_functions.asp)
* 
I will not be going into detail into what these are because the links explain it much better than I ever could.
<br/>
Sudoku 

notes - [cool lady](https://github.com/kying18/sudoku/blob/main/sudoku.py)
<br/>

# ***Skateboard_CAD***
In this assingment, I had to use all of the tools that I have previously used when doing CAD to create a skateboard. I had to create the deck, trucks, and wheels and bearings all separately, as well as put it all together with mates and screws. This assignment also required me to show the different weights along the way, and I was fully on-point the whole time.
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/FullView.png" alt="alt text" width="500" height="500">
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/TrucksBaseplate.png" alt="alt text" width="500" height="400">
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/TruckHanger.png" alt="alt text" width="500" height="500">
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Bushing.png" alt="alt text" width="500" height="400">
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/WheelandBearing.png" alt="alt text" width="500" height="500">

### Reflection
This assignment was fairly easy, however I did learn some new things. I learned many new shortcuts for selecting dimensions, viewing the sketch plane, and selecting different tools. I also learned about using the "Use" tool, which i had known about but did not know the full extend of. In the end, however, the entire concept of the project is very similar to all other CAD projects. 

# ***Legos!***
In this assignment, we were tasked with creating several configurations for legos, and this allowed us to create anything, including ducks. We first were to create a generic lego brick, and then we added all of the possible configurations for the different legos.

<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Duck.png" alt="alt text" width="500" height="500">

<br/>

I then had to take the legos I created and create something of my own, so I made a house.

<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/house.png" alt="alt text" width="500" height="500">

<br/>
<br/>

# ***Multi-Tool***
### Description
The point of this assignment was to use all of the CAD knowledge that we had gained in the previous assignments to create a fully working Multi-Tool. The schematics for the tool were given to use via Canvas, and all we had to do was create the 
### Evidence
The link to view the Onshape document is [here](#https://cvilleschools.onshape.com/documents/d920a05953c045faf0336f45/w/f8b84a33a05b2bdaca91bbc5/e/bcc80d60cab3728939386329). The assignemnt looks something like this: 
<br/>

<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/Multitool.png" alt="alt text" width="500" height="500">

### Reflections

This assignment was almost identical to all of the other CAD assignments, as they all revolved around small geometry problems and problem solving for dimensions not directly provided.

---
# ***Pi LED Blink***
### Description
In this assignment, I had to learn how to use the Pi T-Cobbler, along with reassociating myself with all of the wiring. This included LEDs, resistors, etc.
### Wiring // Evidence
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/blinkygif.gif" alt="alt text" width="500" height="500">

### Code

this is the [code](https://github.com/willhk10/Engineering_4_Notebook/blob/main/Python/blink2leds.py) for the assignment. It is very straightforward, as it is a simple while loop that changes the output states of the two leds.
### Reflections
---

# ***Shutdown Button***
### Description
The basic premise of this assingment is to create a button that allows you to both shutdown and restart your pi with either a press or a hold. This allows you to have a safe shutdown if you want to make your pi headless, or if you want to restart your pi without a serial monitor.
### Wiring

<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/image_67174401.JPG" alt="alt text" width="500" height="500">

### Evidence

<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/ShutdownButton.gif" alt="alt text" width="500" height="500">

### Reflections
This assignment was not very difficult, although I had to go through a lot of frustration when troubleshooting, as there were many moving parts that could have been faulty. The button, the code, the pi, and the wiring of the button were all possible faults. When I eventually found a small bug in my code, the button worked perfectly.

---
# ***GPIO Pins - Introduction***
### Description
The main point of this assignment is to get accustomed to using the T-Cobbler with different devices, such as the accelerometer. In this assignment, I turned on two LEDS and got them to alternate blinking using a T-Cobbler and the different GPIO pins. 

### Wiring
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/image_67174401.JPG" alt="alt text" width="500" height="500">

### Evidence
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/blinkygif.gif" alt="alt text" width="500" height="500">


### Reflections

This assignment was rather easy, as it was simple coding and following instructions on Canvas. There was little to no creative challenge, as it was more of a setup for future creative assignments.

---
# ***GPIO Pins - I2C***
### Description
The point of this assingment was to both get the accelerometer working and printing out information to the serial monitor, but also to use an OLED monitor to create a graph of the movement of the accelerometer along the ground.
### Wiring
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/image_67174401.JPG" alt="alt text" width="500" height="500">

### Evidence
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/AccelGif1.gif" alt="alt text" width="500" height="500">

### Reflections
This assignment was not easy, as I had to re-familiarize myself with various coding forms and functions I was not used to using, and different syntaxes for the new libraries. 

---

# ***Headless Accelerometer***
### Description
The point of this assignment was to use the system settings of the Pi to have the accelerometer assignment code run as soon as the pi turns on, without any initiation of code or login into the pi. This allows the owner of the pi to connect the pi to a batter and not worry about having to run code into the pi every time there is a restart.
### Wiring
<img src="https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/image_67174401.JPG" alt="alt text" width="500" height="500">

### Evidence
### Reflections
This assignment was not difficult at all, as it was simply setting the default code to run to be the code on my Github that ran the accelerometer and OLED screen. 

---

# ***Camera***
### Description
The point of this assignment was to get the simple Pi camera working to take pictures and print them all to a github folder called Pictures. Another piece of the assignment was to mess with the code a little bit and have it take many different pictures, all with different filters from the PiCamera library. Then, by using the code from the shutdown button assignment, we had to create a stopmotion movie that would take pictures through a button press.

### Evidence
<details><summary><b>Pi Camera Pictures</b></summary><br/>
<IMG SRC="Pictures/picturewithdenoise.jpg" width = "250" height = "188"><IMG SRC="Pictures/picturewithemboss.jpg" width = "250" height = "188"><IMG SRC="Pictures/picturewithnegative.jpg" width = "250" height = "188"><IMG SRC="Pictures/picturewithsketch.jpg" width = "250" height = "188"><IMG SRC="Pictures/picturewithsolarize.jpg" width = "250" height = "188">
<br/></details>

### StopMotion movie:

<img src= "https://github.com/willhk10/Engineering_4_Notebook/blob/main/Pictures/TestProj1/ScreenRecording.gif" alt = "alt text" width="500" height="500">

### Reflections
This assignment was very simple, as the code was rather straightforward, and the wiring was as simple as plugging in a ribbon connector in to the pi ***(when it is turned off)***. Then, by using a for loop I could cycle through all of the effects I wanted to use, and I could create a new image file for each image taken, and send it to the [Pictures](#https://github.com/willhk10/Engineering_4_Notebook/tree/main/Pictures) folder in my github. The Stopmotion movie was very simple, as it only required slight modification of the shutdown button code and the implimentation of the camera taking a photo where the shutdown command would have been



# [Back To Top](#Engineering_4_Notebook)
