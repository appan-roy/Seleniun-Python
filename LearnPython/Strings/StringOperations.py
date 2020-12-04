# To find length of a string, use len(str)
str = "Hello world!"
print(len(str))

# Spaces can be trimmed using strip function but only leading and trailing spaces
p = "   Hello World !!   "
print(p)
print(p.strip())

# A string character can be replaced as mentioned below
print(p.replace("e", "a"))

# To find the index of a letter. There are actually two o's in the phrase - this method only recognizes the first.
print(str.index("o"))

# To find the no. of occurence of a particular number.
print(str.count("l"))

# Indexing in python
print(str[0])   # prints first char
print(str[-1])  # prints last char

# Slicing in python
# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. 
# The general form is [start:stop:step]
print(str[3:7])
print(str[3:7:1])

# With the above mentioned type of slice syntax you can easily reverse a string like this
print(str[::-1])

# These make a new string with all letters converted to uppercase and lowercase
print(str.upper())
print(str.lower())

# Condition checking in strings
print(str.isupper())    # False
print(str.islower())    # False

# This is used to determine whether the string starts with something or ends with something, respectively. 
# The first one will print True, as the string starts with "Hello". The second one will print False, 
# as the string certainly does not end with "asdfasdfasdf"
print(str.startswith("Hello"))
print(str.endswith("asdfasdfasdf"))

# This splits the string into a bunch of strings grouped together in a list. Since this example splits at a space, 
# the first item in the list will be "Hello", and the second will be "world!".

afewwords = str.split(" ")
print(afewwords)

# Exercise
s = "Strings are awesome!"
print("Length of s = %d" % len(s))
print("The first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
print("String in uppercase: %s" % s.upper())
print("String in lowercase: %s" % s.lower())
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
print("Split the words of the string: %s" % s.split(" "))
