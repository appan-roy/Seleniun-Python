""" WAP to print the n-th term of the following series------
2,5,10,17,……  """

import math

n = int(input("Please enter the term : "))

t = 0

for i in range(1, n+1, 1):
    t = math.pow(i, 2) + 1

print("The %d-th term of the series is %d" %(n, t))