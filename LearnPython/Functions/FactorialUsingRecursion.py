""" WAP to find the factorial of a no. using recursion """

def factorial(n):
    if n == 0:  return 1
    else:   return n * factorial(n-1)

num = int(input("Please enter a number : "))
print("The factorial is %d" %factorial(num))