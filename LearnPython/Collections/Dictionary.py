# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, which is any type of object 
# (a string, a number, a list, etc.) instead of using its index to address it.

# For example, a database of phone numbers could be stored using a dictionary like this
phonebook = {}
phonebook["John"] = 9384775566
phonebook["Jack"] = 9383772864
phonebook["Jill"] = 9476627831
print(phonebook)
print(len(phonebook))       # prints the length of phonebook
print(type(phonebook))      # prints the data type of phonebook

# Alternatively, a dictionary can be initialized with the same values in the following notation
phonebook = {
    "John" : 9384775566,
    "Jack" : 9383772864,
    "Jill" : 9476627831
}
print(phonebook)
print(phonebook["Jill"])        # To get Jill's Number
print(phonebook.get("John"))    # To get John's Number using get method
print(phonebook.keys())         # To get all the keys
print(phonebook.values())       # To get all the values
print(phonebook.items())        # To get all the {K, V} pairs

for x in phonebook:
    print(x)                    # prints all the keys
for x in phonebook:
    print(phonebook[x])         # prints all the values
for x, y in phonebook.items():
    print(x, y)                 # prints all the {K, V} pairs

phonebook["Jack"] = "9567398465"     # updating an existing value
print(phonebook)

phonebook["Lilly"] = "9594768638"     # Adding a new item in the dictionary
print(phonebook)

phonebook.pop("John")           # removes a particular item "John"
print(phonebook)

phonebook.popitem()             # removes the last item
print(phonebook)

del phonebook["Jack"]          # deletes a particular item "Jack"
print(phonebook)

phonebook.clear()               # clears the entire dictionary
print(phonebook)

# del phonebook                   # deletes the entire dictionary
# print(phonebook)                # this will throw error as the dictionary is not defined

# To iterate over key value pairs, use the following syntax
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# To remove a specified index, use either one of the following notations
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

# Alternatively use the below for deleting index
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
print(phonebook)

# Dictionary values as a list
emp = {"QA":["Divyangana", "Kanika", "Mandira"], "Dev":"Anish", "Build":"Komal"}
print(emp)
print(emp["QA"])        # ['Divyangana', 'Kanika', 'Mandira']
print(emp["QA"][0])     # Divyangana
print(emp.get("QA"))    # ['Divyangana', 'Kanika', 'Mandira']

# Nested dictionary
emp1 = {"QA":{"ST":"Divyangana", "BAT":"Mandira"}, "Dev":"Anish", "Build":"Komal"}
print(emp1)
print(emp1["QA"])                   # {'ST': 'Divyangana', 'BAT': 'Mandira'}
print(emp1["QA"]["ST"])             # Divyangana
print(emp1.get("QA"))               # {'ST': 'Divyangana', 'BAT': 'Mandira'}
print(emp1.get("QA").get("BAT"))    # Mandira

# Another way of creating a dictionary
emp2 = dict(QA = "Swati", Qa = "Anita", qA = "Priyanka", qa = "Shruti")
print(emp2)

# Another way of creating a dictionary using list and tuple
emp3 = dict([(1, "Java"), (2, "Python"), (3, "JavaScript")])
print(emp3)