# To define an integer, use the following syntax:
myint = 7
print(myint)

# The type of an variable can be checked as below
a = 4
b = 3.5
c = 4j
d = 'Appan'
e = True

print (type(a))     # prints int
print (type(b))     # prints float
print (type(c))     # prints complex
print (type(d))     # prints str
print (type(e))     # prints bool

# Casting can be done of a variable as mentioned in the following way 
x = int (2.4)
y = float (3)
z = str (10)

print(x)   # prints 2
print(y)   # prints 3.0
print(z)   # prints 10 but here 10 is a string, not an integer

# To define a floating point number, use one of the following notations:
myfloat = 8.0
print(myfloat)
myfloat = float(9)
print(myfloat)

# Strings are defined either with a single quote or a double quotes.
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# The difference between the two is that using double quotes makes it easy to include apostrophes 
# (whereas these would terminate the string if using single quotes)
mystring = "Don't worry about apostrophes"
print(mystring)

# To print anything using double quotes, use escape sequence
mystr = "\"Python\""
print(mystr)

# Checking condition
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

# Checking condition
mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)

# The isinstance() function checks if the object (first argument) is an instance or subclass of 
# classinfo class (second argument). The syntax of isinstance() is: isinstance(object, classinfo)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)