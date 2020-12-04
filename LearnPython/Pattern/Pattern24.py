""" 
				1		
			2		2		
		3		3		3		
	4		4		4		4		
5		5		5		5		5		
		6		6		6		
				7
 """

for i in range(1, 6, 1):
    for j in range(i, 5, 1):
        print("\t", end="")
    for k in range(1, i+1, 1):
        print(str(i)+"\t\t", end="")
    print()

for x in range(6, 8, 1):
    for y in range(x, 5, -1):
        print("\t\t", end="")
    for z in range(1, 5-((x-5)*2)+1, 1):
        print(str(x)+"\t\t", end="")
    print()