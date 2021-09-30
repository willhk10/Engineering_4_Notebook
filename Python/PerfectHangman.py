
# Online Python - IDE, Editor, Compiler, Interpreter
err1 = "---┐ \n   O \n  \|/ \n   | \n  /  "
err2 = "---┐ \n   O \n  \|/ \n   | \n   "
err3 = "---┐ \n   O \n  \|/ \n    "
err4 = "---┐ \n   O \n  \| "
err5 = "---┐ \n   O \n  \ "
err6 = "---┐ \n   O \n   "
err7 = "You killed him!"
a = 0
b = 0
CorrectGuess = " "
f = " "
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


word = input("what is your word, player one?")
blanks = "_" * len(word)
seperator = " "

def showguesses(b, Correctguesses, blanks):
    #Correctguesses = ["a","m","e"]
    for Correctguesses in word: #repeat the amount of time that the guesses are in the word
        if Correctguesses == word[b]: #if the guess is the same as the current letter being checked in the original word, do the following code
            blanks = blanks[:b] + word[b] + blanks[b + 1:] #changing the blank line to the correct guess
    return blanks


print("---┐ \n   O \n  \|/ \n   | \n  / \ ")

Misguess = ""
Correctguesses = ""

while True: # loop
    guess2 = input("What is your guess, player 2: ") 
    if len(guess2) != 1: 
    #preventing more than 1 letter guesses
        print("Don't give me 2 letters")
        continue
    if guess2 in word: 
        CorrectGuess = True
    if guess2 not in word:
        CorrectGuess = False
        
    if CorrectGuess == False:
        if guess2 in Misguess:
# preventing duplication of guesses
            print("Already did that one: Try again.") 
            continue
        Misguess = (Misguess + " " + guess2) #defining the missguess and adding in a new misguess every iteration
        print(guess2 + " is incorrect.")
        print("current missed guesses: " + Misguess)
        a = a + 1 # adds one to a everytime there is a false guess, which then goes into the errors function.
        errors(a)
        if a == 7: # if max number of guesses reached
            errors(a)
            print("You lost")
            break
    
    if CorrectGuess == True:
        if guess2 in Correctguesses:
# preventing duplication of guesses
            print("Already guessed that, it worked. Try again pls")
            continue
        Correctguesses = (Correctguesses +  guess2)
       #creating a list of correctguesses, adds in the new correct guess every repetition
        b = 0
        print(" Nice!")
        for guess in word:
            guess = guess2
         #This code checks through the word to see if the guess is equal to any letters in the word, and 
            val = word[b]
            if val == guess: #if it's true then it goes into the showguesses function 
                blanks = showguesses(b, Correctguesses, blanks)
                f = seperator.join(blanks) #This adds in a space inbetween the dashes
                             #if it's false then it goes to the next letter by adding 1 to b, which is the position in the word
            b = b + 1
        print(f)
        
        if Misguess == "":
            print("No incorrect guesses")
        else:
            print(Misguess + " " + "is incorrect")
            print("current missed guesses: " + Misguess)
        if blanks == word: #if finished
                break
