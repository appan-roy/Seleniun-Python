import os

# if the file is opened using with block then outside this block the file will be closed automatically
with open("FileHandling//Demo.txt") as f:
    print("State of the file close is",f.closed)    # file is closed - False
    data = f.read()
    print(data)

print("State of the file close is",f.closed)    # file is closed - True

# using os current directory
with open(os.getcwd()+"\\FileHandling\\Demo.txt") as f:
    print("State of the file close is",f.closed)    # file is closed - False
    data = f.read()
    print(data)

print("State of the file close is",f.closed)    # file is closed - True