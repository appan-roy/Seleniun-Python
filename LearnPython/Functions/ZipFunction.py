# Zip using lists
name = ["Debjani", "Ayshee", "Srimanti"]
phone = [111, 222, 333]
city = ["Bangalore", "Mumbai", "Kolkata"]

data = zip(name, phone, city)
my_data = list(data)
print(my_data)  # ordered output

# unpacking zip
a, b, c = zip(*my_data)
print(a)
print(b)
print(c)

# Zip using sets
name = {"Debjani", "Ayshee", "Srimanti"}
phone = {111, 222, 333}
city = {"Bangalore", "Mumbai", "Kolkata"}

data = zip(name, phone, city)
my_data = list(data)
print(my_data)  # unordered output as set is used

# unpacking zip
a, b, c = zip(*my_data)
print(a)
print(b)
print(c)