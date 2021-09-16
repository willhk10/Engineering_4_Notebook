
from math import sqrt

def doMath(a, b, c):
    discrim = int((b*b)- 4 * a * c)
    if discrim >= 0:
        root1 = int(-b + sqrt((b*b)- 4 * a * c))/ (2* a)
        root2 = int(-b - sqrt((b*b)- 4 * a * c))/ (2* a)
        discrim = int((b*b)- 4 * a * c)
        roots = [root1, root2]
        return roots, discrim 
    if discrim < 0:
        return "", discrim
while True:
    a = int(input("Enter coefficient for a^2 "))
    b = int(input("Enter coefficient for b"))
    c = int(input("enter the constant value"))
    
    (roots, discrim) = doMath(a, b, c)
    if discrim >= 0:
        print("root 1: " + str(roots[0]))
        print("root 2: " + str(roots[1]))
    else:
        print("No Real Roots")
    
