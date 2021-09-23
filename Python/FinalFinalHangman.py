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

def showguesses(b, Correctguesses, blanks):
    #Correctguesses = ["a","m","e"]
    for Correctguesses in word:
        if Correctguesses == word[b]:
            blanks = blanks[:b] + word[b] + blanks[b + 1:]
    print(blanks)
    return blanks

print("---┐ \n   O \n  \|/ \n   | \n  / \ ")

Misguess = ""
Correctguesses = ""

while True:
    guess2 = input("What is your guess, player 2: ")
    if len(guess2) != 1:
        print("Don't give me 2 letters")
        continue
    if guess2 in word: 
        CorrectGuess = True
    if guess2 not in word:
        CorrectGuess = False
        
    if CorrectGuess == False:
        if guess2 in Misguess:
            print("Already did that one: Try again.")
            continue
        Misguess = (Misguess + " " + guess2)
        print(guess2 + " is incorrect.")
        print("current missed guesses: " + Misguess)
        a = a + 1
        errors(a)
        if a == 7:
            errors(a)
            print("You lost")
            break
    
    if CorrectGuess == True:
        if guess2 in Correctguesses:
            print("Already guessed that, it worked. Try again pls")
            continue
        Correctguesses = (Correctguesses +  guess2)
        b = 0
        print(" Nice!")
        for guess in word:
            guess = guess2
            val = word[b]
            if val == guess:
                blanks = showguesses(b, Correctguesses, blanks)
            b = b + 1
            
        if Misguess == "":
            print("No incorrect guesses")
        else:
            print(Misguess + " " + "is incorrect")
            print("current missed guesses: " + Misguess)
        if blanks == word:
                break