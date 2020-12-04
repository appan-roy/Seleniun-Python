# Raise is a custom exception which we can create if certain conditions are not met
num = int(input("Please enter a number : "))

if num == 0:
    raise AssertionError