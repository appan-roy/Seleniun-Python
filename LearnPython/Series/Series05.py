""" WAP to find the sum of the given series---------
S = (1) + (1+2) + (1+2+3) + ……upto n terms """

n = int(input("Please enter the term : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(", end="")
    for j in range(1, i+1, 1):
        if j != i:  print(j, end="+")
        else:   print(j, end="")
        sum += j
    print("), ", end="")
    
print()
print("The sum of the series upto %d-th term is %d" %(n, sum))