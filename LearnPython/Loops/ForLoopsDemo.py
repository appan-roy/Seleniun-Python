# For loops iterate over a given list.
primes = [2, 3, 5, 7]
for x in primes:
    print(x)

# For loops iterate over a given set.
mySet = {6, 'Python', 2.9, True}
for i in mySet:
    print(i)

# For loops iterate over a given dictionary.
myDict = {1:"Python", 2:"Java", 3:"JS"}
for i in myDict:
    print(i)        # to print the keys
for j in myDict.values():
    print(j)        # to print the values
for i,j in myDict.items():
    print(i)        # to print the keys
    print(j)        # to print the values

# For loops iterate over a given tuple.
myTuple = (6, 'Python', 2.9, True)
for i in myTuple:
    print(i)

# Range(5) means x will start from 0 and will iterate the loop by 1 till 4, i.e., < 5.
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Range(3, 6) means x will start from 3 and will iterate the loop by 1 till 5, i.e., < 6.
# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Range(3, 8, 2) means x will start from 3 and will iterate the loop by 2 till 7, i.e., < 8.
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

# For loop example using values from list
num = [1,2,3,4,5]
sum = 0
for val in num:
    sum = sum + val
print("The total is ", sum)

# For loop with else block
fruits = ["apple", "grapes", "orange"]
for val in fruits:
    print(val)
else:
    print("No fruits left")

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# Nested for loops
l1 = [1, 2, 3]
l2 = ['Python', 'Java', 'JS']
for i in l1:
    for j in l2:
        print(str(i)+"|"+j)

# For loop with list of tuples using tuple unpacking
t1 = (1, 2, 3)
t2 = (10, 20, 30)
t3 = (100, 200, 300)
myList = [t1, t2, t3]
print(myList)
for x, y, z in myList:
    print(x)
    print(y)
    print(z)