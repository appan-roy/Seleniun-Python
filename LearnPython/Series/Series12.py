""" WAP to find the sum of the given series---------
S = 1^10 + 2^9 + 3^8 + 4^7 + ……… + 10^1 """

import math

n = int(input("Please enter the term : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(", end="")
    print(i, end="")
    print("^", end="")
    print((11-i), end="")
    print("), ", end="")
    sum += math.pow(i, (11-i))
    
print()
print("The sum of the series upto %d-th term is %d" %(n, sum))