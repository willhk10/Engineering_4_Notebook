
#Python Program 01
#Made By William Keenan
#9.14.21

a = int(input('Enter 1st number: ')) 
b = int(input('Enter 2nd number: '))


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
        
print("CALCULATOR PROGRAM") #                 \/ ALL LINES OF FUNCTION CALLED ONE AT A TIME \/
print("Sum:\t\t" + str(doMath(a,b,1))) 
print("Difference:\t" + str(doMath(a,b,2)))
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
print("Factorial1:\t\t" + str(doMath(a,b,6)))
print("Factorial2:\t\t" + str(doMath(a,b,7)))
