# Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an 
# expression is compared or evaluated.
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x != 5) # prints out True
print(x < 3) # prints out True
print(x > 2) # prints out False

# Conditional statements example if...elif...else
num = 0

if num > 0:
    print("The num is positive")
elif num == 0:
    print("The num is zero")
else:
    print("The num is negative")

# The "and" and "or" boolean operators allow building complex boolean expressions
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# The "in" operator could be used to check if a specified object exists within an iterable object container, 
# such as a list
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# Here is an example for using Python's "if" statement using code blocks
y = 2
if y == 2:
    print("y equals two!")
else:
    print("y does not equal to two.")

# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, 
# but the instances themselves.
a = [1,2,3]
b = [1,2,3]
print(a == b) # Prints out True
print(a is b) # Prints out False

# Using "not" before a boolean expression inverts it
print(not False)                # Prints out True
print((not False) == (False))   # Prints out False

# Exercise
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")

# Another way of if else statement
z = 100
if z == 100: print("Z is equals to 100")
else: print("Z is not equals to 100")

# Shorthand if else statement
print("Z is equals to 100") if z == 100 else print("Z is not equals to 100")