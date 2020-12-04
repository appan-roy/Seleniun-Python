""" 
				1		
		2		2		2		
3		3		3		3		3		
	4		4		4		4		
		5		5		5		
			6		6		
				7
 """

for i in range(1, 4, 1):
    for j in range(i, 3, 1):
        print("\t\t", end="")
    for k in range(1, 2*i, 1):
        print(str(i)+"\t\t", end="")
    print()

for x in range(4, 8, 1):
    for y in range(x, 3, -1):
        print("\t", end="")
    for z in range(1, 9-x, 1):
        print(str(x)+"\t\t", end="")
    print()