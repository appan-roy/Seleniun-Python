""" 
1	3	5	7	9	
3	5	7	9	
5	7	9	
7	9	
9
 """

n = int(input("Please enter the number of terms : "))

for i in range(1, 2*n, 2):
    for j in range(i, 2*n, 2):
        print(str(j)+"\t", end="")
    print()