# Functions are defined using the block keyword "def", followed with the function's name as the block's name.
def my_function():
    print("Hello From My Function!")
my_function()

# Functions also take default arguments if mentioned while defining
def printHi(name = "John"):
        print("Hi, " +name)
printHi("Appan")
printHi()

# Functions may also receive arguments (variables passed from the caller to the function).
def my_function_with_args(username, greeting):
    print("Hello %s, I wish you %s"%(username, greeting))
my_function_with_args("John", "Good morning!")

# Functions may return a value to the caller, using the keyword- 'return'
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(25, 75))

# 1. Add a function named list_benefits() that returns the following list of strings: "More organized code", 
# "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# 2. Add a function named build_sentence(info) which receives a single argument containing a string and 
# returns a sentence starting with the given string and ending with the string " is a benefit of functions!"
# 3. Run and see all the functions work together!
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

# check even number
def check_even_number(num):
    result = (num % 2 == 0)     # result will store boolean value as per condition check
    print(result)
check_even_number(10)

# even and odd number separation
def check_odd_number(list1):
    odd_numbers = []

    for x in list1:
        if x % 2 == 0:
            pass
        else:
            odd_numbers.append(x)

    return odd_numbers

result = check_odd_number([1, 2, 3, 4, 5, 6])

if len(result) > 0:
    print(result)
else:
    print("Sorry !! no odd numbers are found")

# arbitrary arguments - we can use *args if we don't know the function signature
def print_name(*args):
    print(args)     # shows output as a tuple
    for name in args:
        print(name)
print_name("Java", "JS", "Python")

# Get sum of some numbers, max and min numbers
def get_sum(*args):
    print(sum(args))
def get_max_number(*args):
    print(max(args))
def get_min_number(*args):
    print(min(args))
get_sum(10, 45, 87, 28, 5)          # 175
get_max_number(10, 45, 87, 28, 5)   # 87
get_min_number(10, 45, 87, 28, 5)   # 5

# arbitrary keyword arguments - we can use **kwargs if we don't know the function signature
def print_names(**kwargs):
    print(kwargs)       # shows output as a dictionary
    print(type(kwargs))
    print(kwargs["phone"])
print_names(name='Shreyashi', address='Kolkata', phone='99999')

# with both *args and *kwargs
def hello(*args, **kwargs):
    print(args)     # (1, 2, 3)
    print(kwargs)   # {'name': 'Divyangana', 'city': 'Howrah'}
hello(1, 2, 3, name='Divyangana', city='Howrah')

# *args, **kwargs and other arguments altogether
def hello2(first, *args, **kwargs):
    print(first)    # 1
    print(args)     # (2, 3)
    print(kwargs)   # {'name': 'Divyangana', 'city': 'Howrah'}
hello2(1, 2, 3, name='Divyangana', city='Howrah')