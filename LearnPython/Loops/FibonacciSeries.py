""" WAP to print the Fibonacci series upto n-th term. """

num = int(input("Please enter the number of terms : "))

t1 = 1
t2 = 0
sum = 0

print("The Fibonacci series upto %d terms is : " %num)
for i in range(0, num, 1):
    print("%d\t" %sum, end =" ")    # to print without new line
    sum = t1 + t2
    t1 = t2
    t2 = sum