# Functions are defined using the block keyword "def", followed with the function's name as the block's name.
def my_function():
    print("Hello From My Function!")
my_function()

# Functions also take default arguments if mentioned while defining
def printHi(name = "John"):
        print("Hi, " +name)
printHi("Appan")
printHi

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
