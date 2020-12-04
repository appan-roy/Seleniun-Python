# Objects are an encapsulation of variables and functions into a single entity. 
# Objects get their variables and functions from classes. Classes are essentially a template to create your objects.
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the first class.")

# To assign the above class(template) to an object you would do the following
myobjectx = MyClass()

# To access the variable inside of the newly created object "myobjectx" you would do the following
x = myobjectx.variable
print(x)

# You can create multiple different objects that are of the same class(have the same variables and functions defined). 
# However, each object contains independent copies of the variables defined in the class. For instance, 
# if we were to define another object with the "MyClass" class and then change the string in the variable above
class MySecondClass:
    variable = "Hello"

    def function(self):
        print("This is a message inside the second class.")

myobjectx = MySecondClass()
myobjecty = MySecondClass()

myobjecty.variable = "World"    # overriding the variable value

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# To access a function inside of an object you use notation similar to accessing a variable
class MyThirdClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the third class.")

myobjectx = MyThirdClass()

myobjectx.function()

# There is a default function (aka constructor) __init__ in every class. We can pass arguments in __init__ and the arguments will
# replace the previous arguments with same parameter. Here name is parameterized as Appan but later while creating
# the class object c the name is pass John so name will be replaced as John. 
class MyFourthClass:
    name = "Appan"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sum(self, a, b):
        print(a+b)
    
c = MyFourthClass("John", 45)
print(c.name)
print(c.age)
print(c.sum(56, 4))

# # Deleting the class object
# d = MyFourthClass("John", 45)
# del d               # Deleting the class object d
# print(d.name)       # This will throw error as the class object is deleted
# print(d.age)        # This will throw error as the class object is deleted
# print(d.sum(56, 4)) # This will throw error as the class object is deleted

# # Deleting the argument of a class object
# e = MyFourthClass("John", 45)
# del e.age           # Deleting the age argument only from class object d
# print(e.name)       
# print(e.age)        # This will throw error as the age argument of the class object is deleted


# We have a class defined for vehicles. Create two new vehicles called car1 and car2. 
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, 
# and car2 to be a blue van named Jump worth $10,000.00.

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())