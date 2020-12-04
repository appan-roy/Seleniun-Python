""" 
				5	
			4	5	
		3	4	5	
	2	3	4	5	
1	2	3	4	5
 """

n = int(input("Please enter the number of terms : "))

for i in range(n, 0, -1):
    for j in range(1, i, 1):
        print("\t", end="")
    for k in range(i, n+1, 1):
        print(str(k)+"\t", end="")
    print()