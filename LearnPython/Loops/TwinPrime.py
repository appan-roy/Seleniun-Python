""" WAP to accept two no.s and check whether they are twin prime no.s or not. 
(Twin prime no.s are the prime no.s whose difference is 2,e.g. (11,13),(17,19) etc) """

import math

num1, num2 = input("Please enter two numbers : ").split()
n1 = int(num1)
n2 = int(num2)

flag1 = 0
flag2 = 0

if n1 <= 1 or n2 <= 1:
    print("Sorry !! You have entered a wrong input. Please try again.")
else:
    for i in range (2, n1, 1):
        if n1 % i == 0:
            flag1 = 1
    for j in range (2, n2, 1):
        if n2 % j == 0:
            flag2 = 1

if flag1 == 0 and flag2 == 0:
    print("Both the numbers are prime")
    if int(math.fabs(n1 - n2)) == 2:
        print("The numbers are twin prime")
    else:
        print("The numbers are not twin prime")
else:
    print("Either of the numbers or both are not prime")