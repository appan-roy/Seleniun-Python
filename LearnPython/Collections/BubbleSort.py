""" WAP to sort a list using Bubble Sort technique. """

myList = (input("Please enter the list of integers : ")).split()
li = []
for item in myList:
    li.append(int(item))

print("The list items to be sorted are : ")
for i in range(0, len(li), 1):
    print(str(li[i])+"\t", end="")

for i in range(0, len(li), 1):
    for j in range(i+1, len(li), 1):
        if li[i] > li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print("\nThe sorted list items are : ")
for i in range(0, len(li), 1):
    print(str(li[i])+"\t", end="")