""" WAP to search an element in a list using Binary Search. If present, also display the position of the 
number in the list. """

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

num = 90
flag = 0
beg = 0
end = len(li)-1

while(beg <= end):
    mid = int((beg + end) / 2)
    if num > li[mid]:
        beg = mid + 1
    elif num < li[mid]:
        end = mid - 1
    else:
        flag = 1
        break

if flag == 1:
    print("The number "+str(num)+" is present in the list at "+str((mid+1))+"-th position")
else:
    print("The number "+str(num)+" is not present in the list")