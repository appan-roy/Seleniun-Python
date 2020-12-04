""" WAP to find the sum of the given series---------
S = 1 + 3 + 5 + ……. + (2n-1) """

n = int(input("Please enter the term : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, 2*n, 2):
    print(i, end="  ")
    sum += i

print()
print("The sum of the series upto %d-th term is %d" %(n, sum))