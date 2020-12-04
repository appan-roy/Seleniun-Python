# Defining a tuple
my_tuple = ("Apple", "Orange", "Litchi")
print(my_tuple)                 # prints the whole tuple
print(my_tuple[1])              # prints the element at index 1
print(my_tuple[-1])             # prints the last element as negative indexation starts from the last
print(my_tuple[0:2])            # prints the elements in range 0-to-1
print(len(my_tuple))            # prints the length of the tuple
print(type(my_tuple))           # prints the data type of the tuple
print(my_tuple.count("Apple"))  # prints the count of number of occurence of the item
print(my_tuple.index("Litchi")) # prints the index of the item

for val in my_tuple:
    print(val)

# del my_tuple            # deleting the tuple
# print(my_tuple)         # this will throw error as the tuple has been deleted

nested_tuple = ("Apple", ('a', 'b', 'c'), ["New York", "Kolkata", "Johannesburg"])
print(nested_tuple)
nested_tuple[2][2] = "Manchester"   # Changing the existing element. New element add/remove is not allowed in tuple
print(nested_tuple)

# Checking conditions in boolean
print("Apple" in nested_tuple)          # prints True as the element "Apple" exists in the tuple
print("Litchi" in nested_tuple)         # prints False as the element "Litchi" doesn't exist in the tuple

# Tuple conversion into list, set
tup1 = (1, 2.0, "Python", False)
print(type(tup1))

list1 = list(tup1)
print(list1)
print(type(list1))

set1 = set(tup1)
print(set1)
print(type(set1))

# Tuple with single string
tup2 = ("Python")
print(len(tup2))    # here the character count is displayed
tup3 = ("Python",)  
print(len(tup3))    # here the actual element count is displayed as a comma is used in the tuple tup3

# List of tuples
list2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(list2[0])
print(list2[1][2])

# Another way of creating a tuple
tup4 = tuple(['Python', 'JavaScript', 'Java'])
print(tup4)
print(type(tup4))
print(tup4[1])

# Tuple unpacking - number of variable should be equal as the number of elements of the tuple
x, y, z = tup4
print(x)    # Python
print(y)    # JavaScript
print(z)    # Java