""" WAP to create a list with 10 no.s & find how many sets of consecutive no.s are present in 
consecutive pocket. """

myList = (input("Please enter the list of integers : ")).split()
li = []
for item in myList:
    li.append(int(item))

print("The list is : ")
for i in range(0, len(li), 1):
    print(str(li[i])+"\t", end="")

count = 0

for i in range(0, len(li)-1, 1):
    if li[i]+1 == li[i+1]:
        count = count + 1

print("\nThe total number of consecutive sets are : " + str(count))