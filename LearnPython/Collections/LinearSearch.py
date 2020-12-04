""" WAP to search an element in a list using Linear Search. If present, also display the position of the number
in the list. """

myList = (input("Please enter the list of integers : ")).split()
li = []
for item in myList:
    li.append(int(item))

print("The list is : ")
for i in range(0, len(li), 1):
    print(str(li[i])+"\t", end="")

flag = 0

num = int(input("\nPlease enter the number you want to search : "))

for i in range(0, len(li), 1):
    if num == li[i]:
        flag = 1
        break

if flag == 1:   print("The number "+str(num)+" is present in the list at "+str((i+1))+"-th position")
else:   print("The number "+str(num)+" is not present in the list")