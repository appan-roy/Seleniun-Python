""" WAP to check whether a no. is prime or not. """

num = int(input("Please enter a number : "))

flag = 0

if num < 1:
    print("Sorry !! You have entered a wrong input. Please try again.")
elif num == 1:
    print("The number is not a prime number")
else:
    for i in range(2, num, 1):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")