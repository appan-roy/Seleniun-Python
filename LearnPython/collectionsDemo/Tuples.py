# Defining a tuple
my_tuple = ("Apple", "Orange", "Litchi")
print(my_tuple)         # prints the whole tuple
print(my_tuple[1])      # prints the element at index 1
print(my_tuple[-1])     # prints the last element as negative indexation starts from the last
print(my_tuple[0:2])    # prints the elements in range 0-to-1
print(len(my_tuple))    # prints the length of the tuple

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
