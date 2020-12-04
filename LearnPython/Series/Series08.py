""" WAP to find the sum of the given series---------
S = 1 - 1/2! + 1/3! - 1/4! + ……upto n terms """

n = int(input("Please enter the term : "))

sum = 0
f = 1

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    print("(1/", end="")
    print(i, end="")
    print("!), ", end="")
    f *= i
    if i % 2 == 0:  sum -= 1/f
    else:   sum += 1/f
    
print()
print("The sum of the series upto %d-th term is %f" %(n, sum))