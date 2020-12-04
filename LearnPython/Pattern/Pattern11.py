""" 
5	4	3	2	1	
4	3	2	1	
3	2	1	
2	1	
1	
2	1	
3	2	1	
4	3	2	1	
5	4	3	2	1
 """

n = int(input("Please enter the number of terms : "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(str(j)+"\t", end="")
    print()

for x in range(2, n+1, 1):
    for y in range(x, 0, -1):
        print(str(y)+"\t", end="")
    print()