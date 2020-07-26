# For loops iterate over a given sequence.
primes = [2, 3, 5, 7]
for x in primes:
    print(x)

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

# While loops repeat as long as a certain boolean condition is met
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

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

# While Loop Example. The sum of n numbers
print("Enter a number: ")
num = int(input())
sum = 0
counter = 1

while counter < num:
    sum = sum + counter
    counter = counter + 1
print("The total is ", sum)

# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, 
# and return to the "for" or "while" statement
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If break statement is executed inside for loop then the "else" part is skipped. 
# Note that "else" part is executed even if there is a continue statement.
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
