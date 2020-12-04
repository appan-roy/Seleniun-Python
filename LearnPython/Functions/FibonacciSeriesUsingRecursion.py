""" WAP to display the Fibonacci series using recursion """

def fibonacci(n):
    if n == 0:  return 0
    elif n == 1:    return 1
    else:   return (fibonacci(n-1) + fibonacci(n-2))

num = int(input("Please enter the number of terms : "))
for i in range(0, num, 1):
    print(fibonacci(i), end="   ")