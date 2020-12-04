""" WAP to find the sum of the given series---------
S = 2 - 4 + 6 - 8 +…….upto n terms """

n = int(input("Please enter the term : "))

sum = 0

print("The series upto %d-th term is : " %n)
for i in range(1, n+1, 1):
    if i % 2 == 0:
        j = i * (-2)
        sum += j
        print(j, end="  ")
    else:
        k = i * 2
        sum += k
        print(k, end="  ")

print()
print("The sum of the series upto %d-th term is %d" %(n, sum))