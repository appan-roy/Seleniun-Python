""" Check the triangle is possible or not by using the sides """

# Taking three sides as inputs at a time
strSide1, strSide2, strSide3 = input("Enter the length of three sides of the triangle : ").split()
side1 = int(strSide1)
side2 = int(strSide2)
side3 = int(strSide3)

if (side1+side2) >= side3 and (side2+side3) >= side1 and (side3+side1) >= side2:
    print("Triangle is possible")
    if side1 == side2 and side2 == side3:
        print("The triangle is equilateral")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")
else:
    print("Triangle is not possible")