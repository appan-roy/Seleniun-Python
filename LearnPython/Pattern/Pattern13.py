""" 
1	2	3	4	5	4	3	2	1	
	1	2	3	4	3	2	1	
		1	2	3	2	1	
			1	2	1	
				1	
			1	2	1	
		1	2	3	2	1	
	1	2	3	4	3	2	1	
1	2	3	4	5	4	3	2	1
 """

n = int(input("Please enter the number of terms : "))

for i in range(n, 1, -1):
    for j in range(i, n, 1):
        print("\t", end="")
    for k in range(1, i+1, 1):
        print(str(k)+"\t", end="")
    for l in range(i-1, 0, -1):
        print(str(l)+"\t", end="")
    print()

for x in range(1, n+1, 1):
    for y in range(x, n, 1):
        print("\t", end="")
    for z in range(1, x+1, 1):
        print(str(z)+"\t", end="")
    for w in range(x-1, 0, -1):
        print(str(w)+"\t", end="")
    print()