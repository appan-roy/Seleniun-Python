""" WAP to print the maximum & minimum no. of a list without sorting """

myList = (input("Please enter the list of integers : ")).split()
li = []
for item in myList:
    li.append(int(item))

print("The list is : ")
for i in range(0, len(li), 1):
    print(str(li[i])+"\t", end="")

max = li[0]
min = li[0]

for i in range(0, len(li), 1):
    if li[i] > max:
        max = li[i]
    if li[i] < min:
        min = li[i]

print("\nThe max number : " + str(max) + " and the min number : " + str(min))