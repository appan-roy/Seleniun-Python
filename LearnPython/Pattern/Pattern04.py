""" 
1	2	3	4	5	
	2	3	4	5	
		3	4	5	
			4	5	
				5
 """

n = int(input("Please enter the number of terms : "))

for i in range(1, n+1, 1):
    for j in range(i, 1, -1):
        print("\t", end="")
    for k in range(i, n+1, 1):
        print(str(k)+"\t", end="")
    print()