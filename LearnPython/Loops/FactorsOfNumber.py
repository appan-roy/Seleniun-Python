""" WAP to accept a no. & find all the factors of that no. e.g. 15=1,3,5,15. """

num = int(input("Please enter a number : "))

print("The factors of the number are : \n")
for i in range(1, num+1, 1):
    if num % i == 0:
        print("%d" %i)