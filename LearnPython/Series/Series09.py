""" WAP to find the sum of the given series---------
S = (1+2)/(2*3) + (2+3)/(3*4) + (3+4)/(4*5) + ……upto n terms """

n = int(input("Please enter the term : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(", end="")
    print(i, end="")
    print("+", end="")
    print(i+1, end="")
    print(")/(", end="")
    print(i+1, end="")
    print("*", end="")
    print(i+2, end="")
    print("), ", end="")
    sum += (i+(i+1))/((i+1)*(i+2))
    
print()
print("The sum of the series upto %d-th term is %f" %(n, sum))