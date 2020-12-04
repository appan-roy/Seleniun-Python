""" WAP to check a no. is palindrome or not. e.g. 717 is a palindrome no. """

num = int(input("Please enter a number : "))

final = 0
temp = num

while num > 0:
    rem = num % 10
    num = int(num / 10)
    final = final * 10 + rem

if final == temp:
    print("The number is palindrome")
else:
    print("The number is not palindrome")