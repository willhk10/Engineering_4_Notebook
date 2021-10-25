
from math import sqrt 

def doMath(a, b, c): #define function
    discrim = int((b*b)- 4 * a * c) #find discriminant
    if discrim >= 0: #quadratic formula  
        root1 = int(-b + sqrt((b*b)- 4 * a * c))/ (2* a) #Finding root 1
        root2 = int(-b - sqrt((b*b)- 4 * a * c))/ (2* a) #Finding root 2
        discrim = int((b*b)- 4 * a * c)
        roots = [root1, root2]
        return roots, discrim 
    if discrim < 0: #No value if the discriminant is less than zero
        return "", discrim
while True:
    a = int(input("Enter coefficient for a^2 "))
    b = int(input("Enter coefficient for b"))
    c = int(input("enter the constant value"))
    
    (roots, discrim) = doMath(a, b, c) #Defining the function in the while True: loop
    if discrim >= 0: #restating the first statement
        print("root 1: " + str(roots[0]))
        print("root 2: " + str(roots[1]))
    else:
        print("No Real Roots") 
    
