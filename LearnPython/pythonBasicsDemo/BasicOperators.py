a = 100
b = 30
sum = a + b
subtract = a - b
multiply = a * b
divide = a / b
remainder = a % b
print(sum)
print(subtract)
print(multiply)
print(divide)
print(remainder)

# Using two multiplication symbols makes a power relationship.
sqre = 7**2
cube = 6**3
print(sqre)
print(cube)

# Python supports concatenating strings using the addition operator
hello = "Hello"
world = "World"
helloworld = hello + " " + world
print(helloworld)

# Python also supports multiplying strings to form a string with a repeating sequence
lotsofhellos = "hello" * 10
print(lotsofhellos)

# Lists can be joined with the addition operators
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Console input can be taken as below
print("Enter your name: ")
x = input()
print("Hello " + x + " !!")

# Just as in strings, Python supports forming new lists with a repeating sequence using the multiplication operator
print([1,2,3] * 3)

# The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the 
# variables x and y, respectively. You are also required to create a list called big_list, which contains the 
# variables x and y, 10 times each, by concatenating the two lists you have created.

x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
