""" 
				1	1	1	
			2	2	2	2	2	
		3	3	3	3	3	3	3	
	4	4	4	4	4	4	4	4	4	
5	5	5	5	5	5	5	5	5	5	5
 """

n = int(input("Please enter the number of terms : "))

for x in range(1, n+1, 1):
    for y in range(x, n, 1):
        print("\t", end="")
    for z in range(1, (2*(x+1)), 1):
        print(str(x)+"\t", end="")
    print()