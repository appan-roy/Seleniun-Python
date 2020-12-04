""" WAP to find the sum of the given series---------
S = 1 + 2/3 + 3/6 + 4/10 + 5/15 + …… + upto n terms """

n = int(input("Please enter the term : "))

sum = 0
f = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(", end="")
    print(i, end="")
    f += i
    print("/", end="")
    print(f, end="")
    print("), ", end="")
    sum += i/f
    
print()
print("The sum of the series upto %d-th term is %f" %(n, sum))