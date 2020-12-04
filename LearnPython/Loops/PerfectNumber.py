""" WAP to accept a no. & check whether the no. is perfect or not. e.g. Factors of 6=1,2,3 & also 6=1+2+3.
So 6 is a perfect no. """

num = int(input("Please enter a number : "))

sum = 0

for i in range(1, num, 1):
    if num % i == 0:
        sum += i

if(sum == num):
    print("The number is a perfect number")
else:
    print("The number is not a perfect number")