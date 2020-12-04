""" WAP to check whether a no. is Armstrong or not. (e.g. 153 is an Armstrong no. because 1^3+5^3+3^3=153). 
More example:- 370,371,407. """

import math

num = int(input("Enter a number : "))

sum = 0
temp = num

while num > 0:
    rem = num % 10
    sum += int(math.pow(rem, 3))
    num = int(num / 10)

if sum == temp:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")