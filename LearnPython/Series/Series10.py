""" WAP to find the sum of the given series---------
S = 1 + x + x^2/2! + x^3/3! + …… + x^n/n! """

import math

def factorial(n):
    if n == 0:  return 1
    else:   return n * factorial(n-1)

n = int(input("Please enter the term : "))
x = int(input("Please enter the value of x : "))

sum = 1
p = 1

print("The series upto %d-th term is : " %n)
print("(1), ", end="")
for i in range(1, n, 1):
    print("(", end="")
    print(x, end="")
    print("^", end="")
    print(i, end="")
    print("/", end="")
    print(i, end="")
    print("!), ", end="")
    sum += math.pow(x, i) / factorial(i)
    
print()
print("The sum of the series upto %d-th term is %f" %(n, sum))