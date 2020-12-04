try:
    f = open("FileHandling//Demo.txt")  # oprn file
    data = f.read()     # read the data from file
    print(data)     # print the data
    print(f.name)     # print the file name
    print(f.mode)     # print the file opening mode
    print(f.closed)   # print true if file is closed else false
except FileNotFoundError as err:
    print(err)
except ValueError as err:
    print(err)
except TypeError as err:
    print(err)
else:
    print("No exception occurred")
finally:
    f.close()   # close file
    print(f.closed)   # print true if file is closed else false