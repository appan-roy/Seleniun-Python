""" 
1	
2	1	
3	2	1	
4	3	2	1	
5	4	3	2	1	
4	3	2	1	
3	2	1	
2	1	
1
 """

n = int(input("Please enter the number of terms : "))

for i in range(1, n+1, 1):
    for j in range(i, 0, -1):
        print(str(j)+"\t", end="")
    print()

for k in range(n-1, 0, -1):
    for l in range(k, 0, -1):
        print(str(l)+"\t", end="")
    print()