string = input("Please enter a string : ")

revString = string[::-1]

print("The string is a palindrome") if revString == string else print("The string is not a palindrome")