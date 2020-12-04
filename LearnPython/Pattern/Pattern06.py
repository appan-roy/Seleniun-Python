""" 
1	2	3	4	5	6	7	8	9	
	1	2	3	4	5	6	7	
		1	2	3	4	5	
			1	2	3	
				1
 """

n = int(input("Please enter the number of terms : "))

for i in range(1, n+1, 1):
    for j in range(1, i, 1):
        print("\t", end="")
    for k in range(1, (2*n-1)-((i-1)*2)+1, 1):
        print(str(k)+"\t", end="")
    print()