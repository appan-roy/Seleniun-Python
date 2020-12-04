""" WAP to accept a no. & check:
(a) whether the no. is divisible by 2 & 5
(b) whether the no. is divisible by 2 but not by 5
(c) whether the no. is divisible by 5 but not by 2 """

strNumber = input("Please enter a number : ")
num = int(strNumber)

if num % 2 == 0:
    if num % 5 == 0:
        print("The number is divisible by 2 and 5")
    else:
        print("The number is divisible by 2 but not 5")
elif num % 5 == 0:
    if num % 2 != 0:
        print("The number is divisible by 5 but not 2")
