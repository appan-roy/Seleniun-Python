""" WAP to create a list with 10 no.s. Some no.s are duplicate. Print the duplicate no.s once only. """

myList = (input("Please enter the list of integers : ")).split()
li = []
duplicate = []
for item in myList:
    li.append(int(item))

print("The list is : ")
for i in range(0, len(li), 1):
    print(str(li[i])+"\t", end="")

for i in range(0, len(li), 1):
    flag = 0
    for j in range(i+1, len(li), 1):
        if li[i] == li[j]:
            flag = 1
    if flag == 1:
        duplicate.append(li[i])

print("\nThe duplicate numbers are : ")
for i in range(0, len(duplicate), 1):
    print(str(duplicate[i])+"\t", end="")