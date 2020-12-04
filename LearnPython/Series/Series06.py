""" WAP to find the sum of the given series---------
S = (1*2) + (2*3) + (3*4) + ………upto n terms """

n = int(input("Please enter the term : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(", end="")
    print(i, end="*")
    print(i+1, end="")
    sum += (i*(i+1))
    print("), ", end="")
    
print()
print("The sum of the series upto %d-th term is %d" %(n, sum))