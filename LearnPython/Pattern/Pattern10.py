""" 
1	2	3	4	5	4	3	2	1	
2	3	4	5		5	4	3	2	
3	4	5				5	4	3	
4	5						5	4	
5								5
 """

n = int(input("Please enter the number of terms : "))
m = 1

for x in range(1, n+1, 1):
    if x != 1:
        for i in range(x, n+1, 1):
            print(str(i)+"\t", end="")
        for j in range(m, 0, -1):
            print("\t", end="")
        for k in range(n, x-1, -1):
            print(str(k)+"\t", end="")
        m += 2
    else:
        for y in range(x, n+1, 1):
            print(str(y)+"\t", end="")
        for z in range(n-1, x-1, -1):
            print(str(z)+"\t", end="")
    print()