# Defining a set
my_set = {"Chalk", "Duster", "Board"}
print(my_set)
print(len(my_set))
print(type(my_set))

for x in my_set:
    print(x)

# Copy a set
my_set2 = my_set.copy()
print(my_set2)

# Another way to define a set
set1 = set(['Python', 6, 2.0, 87])      # using set instance with list
print(set1)
set2 = set(('Python', 6, 2.0, 87))      # using set instance with tuple
print(set2)

# Checking conditions in boolean
print("Chalk" in my_set)            # prints True as the element "Chalk" exists in the tuple
print("Litchi" in my_set)           # prints False as the element "Litchi" doesn't exist in the tuple

my_set.add("Pen")                   # Adding an element to the set
print(my_set)
my_set.update(["Eraser", "Pencil"]) # Adding multiple elements to the set
print(my_set)

# Elements can be removed using remove and discard from a set. The difference between the two is as follows
# REMOVE - Use this while you are sure that this element exists in the set. Otherwise, it will throw error
# DISCARD - You can use everytime. It won't throw error even if the element is not present in the set
my_set.remove("Pencil")             # Removing a particular element
print(my_set)
my_set.discard("Pen")               # Removing a particular element
print(my_set)
my_set.pop()                        # Deletes an element at random
print(my_set)
my_set.clear()                      # Clears the entire set
print(my_set)
# del my_set                        # Deletes the entire set
# print(my_set)

nested_set = {"Orange", 'd', 1, 5j, 6.78, (3, 4, 5)}   # Nested set. Tuple is allowed inside a set but list isn't
print(nested_set)

mylist = [1, 2, 3]
print(mylist)
my_set_2 = set(mylist)      # Converts a list to a set
print(my_set_2)

mytuple = (4, 5, 6)
print(mytuple)
my_set_3 = set(mytuple)     # Converts a tuple to a set
print(my_set_3)

# Set operations - UNION, INTERSECTION, DIFFERENCE, SYMMETRIC DIFFERENCE
A = {1, 2, 3, 'a', 'b'}
B = {3, 4, 5, 'b', 'c'}

# UNION
print(A.union(B))
print(A | B)

# INTERSECTION
print(A.intersection(B))
print(A & B)

# DIFFERENCE
print(A.difference(B))
print(A - B)

# SYMMETRIC DIFFERENCE
print(A.symmetric_difference(B))
print(A ^ B)