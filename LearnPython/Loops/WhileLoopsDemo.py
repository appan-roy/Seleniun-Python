# While loops repeat as long as a certain boolean condition is met
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# While Loop Example. The sum of n numbers
print("Enter a number: ")
num = int(input())
sum = 0
counter = 1

while counter <= num:
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

# When the loop condition of "for" or "while" statement fails then code part in "else" is executed. 
# If break statement is executed inside for loop then the "else" part is skipped. 
# Note that "else" part is executed even if there is a continue statement.
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
