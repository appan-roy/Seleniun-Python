# Collection data types - List, Tuple, Set, Dictionary. The differences between them is shown below -
# List        []      Ordered     Indexed     Changeable    Duplicates
# Tuple       ()      Ordered     Indexed     Unchangeable  Duplicates
# Set         {}      Unordered   Unindexed                 No duplicates
# Dictionary  {K:V}   Unordered   Indexed     Changeable    No duplicates

# Defining a list as following
my_list = ["Paris", "London", "New York"]
print(my_list)  # ['Paris', 'London', 'New York']
print(my_list[1])   # London
print(my_list[-1])   # New York
print(len(my_list))
print(type(my_list))

for val in my_list:
    print(val)

# List concatenation
my_second_list = ["Kolkata", "Mumbai", "New Delhi"]
print(my_list+my_second_list)

# Checking conditions in boolean
print("London" in my_list)          # prints True as the element "London" exists in the tuple
print("Litchi" in my_list)         # prints False as the element "Litchi" doesn't exist in the tuple

my_list[2] = "New Delhi"    # Changing the third element of the list
print(my_list)
my_list.insert(3,"Kolkata") # Inserting Kolkata in index 3
print(my_list)
my_list.remove("London")    # Removing London from the list
print(my_list)
my_list.pop()               # Pop removes the last element of a list by default
print(my_list)
my_list.append("Tokyo")     # Appending with Tokyo
print(my_list)
my_list.pop(1)              # Removing the element at index 1
print(my_list)
del my_list[1]              # Deleting the element at index 1
print(my_list)
my_list.clear()             # Clearing the whole list
print(my_list)

fruits = ["apple", "banana", "cherry",]
print(fruits)
fruits.reverse()            # reversing the list
print(fruits)

list_mul_data_type = ["apple", 1, 3, 5j]    # List with multiple data types
print(list_mul_data_type)

nested_list = ["cherry", [1, 2, 3], ['a', 'b', 'c']]    # Nested list example
print(nested_list)
print(nested_list[1])       # Accessing the element at index 1
print(nested_list[1][2])    # Accessing the element at index 1 and then at index 2 of the inner list

# append: Adds its argument as a single element to the end of a list. The length of the list increases by one.
mylist = []
mylist.append(34)
mylist.append(67)
mylist.append(89)
print(mylist[0]) # prints 34
print(mylist[1]) # prints 67
print(mylist[2]) # prints 89

# extend(): Iterates over its argument and adding each element to the list and extending the list.
yourlist = [6, 0, 4, 1] 
mylist.extend(yourlist)
mylist.extend("appan")
print(mylist)   # [34, 67, 89, 6, 0, 4, 1, 'a', 'p', 'p', 'a', 'n']

# In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. 
# You must add the numbers 10,20, and 30 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.
# You will also have to fill in the variable second_name with the second name in the names list, 
# using the brackets operator [].

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(10)
numbers.append(20)
numbers.append(30)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# Slicing of list
list1 = [7, 17, 23, 29, 31]
print(list1[1:3])   # [17, 23]
print(list1[-2])    # 29

# Sorting a list
list2 = [28, 34, 12, 56, 42, 90, 61, 85, 3, 78]

# sort in ascending order
list2.sort()
print(list2)

# sort in descending order
list2.reverse()
print(list2)