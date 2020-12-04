""" WAP to create two lists with 10 elements & check the lists are identical or not. """

myFirstList = (input("Please enter the first list of integers : ")).split()
first = []
for item in myFirstList:
    first.append(int(item))

print("The first list is : ")
for i in range(0, len(first), 1):
    print(str(first[i])+"\t", end="")

mySecondList = (input("\nPlease enter the second list of integers : ")).split()
second = []
for item in mySecondList:
    second.append(int(item))

print("The second list is : ")
for i in range(0, len(second), 1):
    print(str(second[i])+"\t", end="")

count = 0

for i in range(0, len(first), 1):
    for j in range(0, len(second), 1):
        if first[i] == second[j]:
            count = count + 1

if count == len(first):
    print("\nThe lists are identical")
else:
    print("\nThe lists are not identical")