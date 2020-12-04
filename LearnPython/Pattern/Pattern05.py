""" 
				1	
			2	3	2	
		3	4	5	4	3	
	4	5	6	7	6	5	4	
5	6	7	8	9	8	7	6	5
 """

n = int(input("Please enter the number of terms : "))

for i in range(1, 2*n, 2):
    for j in range(1, int(((2*n-1-i)/2)+1), 1):
        print("\t", end="")
    for k in range(int(((i+1)/2)), i+1, 1):
        print(str(k)+"\t", end="")
    for l in range(i-1, int(((i+1)/2)-1), -1):
        print(str(l)+"\t", end="")
    print()