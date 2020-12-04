""" WAP to find the sum of digits of any no. """

num = int(input("Please enter a number : "))

sum = 0
temp = num

while num > 0:
    rem = num % 10
    sum += rem
    num = int(num / 10)

print("The sum of digits of the number %d" %temp + " is %d" %sum)