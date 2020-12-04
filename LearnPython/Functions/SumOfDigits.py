""" WAP to calculate the sum of digits of a 5-digit no. without using recursion """

def sum_of_digits(n):
    p = 0
    while n > 0:
        y = n % 10
        p += y
        n = int(n / 10)
    return p

num = int(input("Please enter a number : "))
print("The sum of the digits of %d" %num + " is %d" %sum_of_digits(num))