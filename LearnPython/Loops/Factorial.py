""" WAP to find the factorial of a no. using while loop. """

num = int(input("Please enter a number : "))

fact = 1
temp = num

while num > 1:
    fact *= num
    num = num - 1

print("The factorial is %d" %fact)