""" 
5	4	3	2	1	
	5	4	3	2	
		5	4	3	
			5	4	
				5	
			5	4	
		5	4	3	
	5	4	3	2	
5	4	3	2	1
 """

n = int(input("Please enter the number of terms : "))

for i in range(1, n+1, 1):
    for j in range(i, 1, -1):
        print("\t", end="")
    for k in range(n, i-1, -1):
        print(str(k)+"\t", end="")
    print()

for x in range(n-1, 0, -1):
    for y in range(x, 1, -1):
        print("\t", end="")
    for z in range(n, x-1, -1):
        print(str(z)+"\t", end="")
    print()