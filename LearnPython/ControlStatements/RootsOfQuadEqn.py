""" The standard form of quadratic equation is given by: ax^2 + bx + c =0; 
where D = b^2 - 4ac, is known as discriminant which determines the nature of the roots:-
If D>0 Roots are real & unequal     [a=3, b=5, c=2]
If D=0 Roots are real & equal       [a=1, b=2, c=1]
If D<0 Roots are imaginary          [a=3, b=2, c=1]
WAP to determine the nature of the roots of a quadratic equation. Also, find the roots of the equation. """

import math

coeff1, coeff2, coeff3 = input("Enter the coefficients of the quadratic equation : ").split()
a = int(coeff1)
b = int(coeff2)
c = int(coeff3)

D = math.pow(b, 2) - 4*a*c

if D > 0:
    print("The roots are real and unequal")
    root1 = (-b + math.sqrt(D)) / 2*a
    root2 = (-b - math.sqrt(D)) / 2*a
    print("The roots are : %.2f" %root1 + " and %.2f" %root2)
elif D == 0:
    print("The roots are real and equal")
    root1 = (-b + math.sqrt(D)) / 2*a
    root2 = (-b - math.sqrt(D)) / 2*a
    print("The roots are : %.2f" %root1 + " and %.2f" %root2)
else:
    print("The roots are imaginary")