""" WAP to print the n-th term of the following series------
1,12,123,1234,………  """

n = int(input("Please enter the term : "))

t = 0

for i in range(1, n+1, 1):
    t = t*10 + i

print("The %d-th term of the series is %d" %(n, t))