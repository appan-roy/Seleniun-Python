""" WAP to find the sum of the given series---------
S = a - a^3/5  + a^5/9 - a^7/13 + ……upto n terms """

import math

n = int(input("Please enter the term : "))
a = int(input("Please enter the value of a : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(", end="")
    print(a, end="")
    print("^", end="")
    print((2*i-1), end="")
    print("/", end="")
    print((4*i-3), end="")
    print("), ", end="")
    if i % 2 == 0:
        sum -= math.pow(a, (2*i-1))/(4*i-3)
    else:
        sum += math.pow(a, (2*i-1))/(4*i-3)
    
print()
print("The sum of the series upto %d-th term is %f" %(n, sum))