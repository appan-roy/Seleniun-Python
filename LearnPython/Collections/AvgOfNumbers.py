""" WAP to calculate the average of a series of no.s using list """

myList = [23, 65, 87, 53, 74]
sum = 0

for i in myList:
    sum += i
avg = sum / len(myList)
print("The sum of the list elements is :", sum)
print("The average of the list elements is :", avg)