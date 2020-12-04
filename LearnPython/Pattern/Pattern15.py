""" 
5								5	
4	5						5	4	
3	4	5				5	4	3	
2	3	4	5		5	4	3	2	
1	2	3	4	5	4	3	2	1	
2	3	4	5		5	4	3	2	
3	4	5				5	4	3	
4	5						5	4	
5								5	
 """

n = int(input("Please enter the number of terms : "))
p = (2*(n-1)-1)
q = 1

for i in range(n, 0, -1):
    if(i != 1):
        for j in range(i, n+1, 1):
            print(str(j)+"\t", end="")
        for k in range(1, p+1, 1):
            print("\t", end="")
        for l in range(n, i-1, -1):
            print(str(l)+"\t", end="")
        p -= 2
    else:
        for m in range(i, n+1, 1):
            print(str(m)+"\t", end="")
        for r in range(n-1, i-1, -1):
            print(str(r)+"\t", end="")
    print()

for x in range(2, n+1, 1):
    for y in range(x, n+1, 1):
        print(str(y)+"\t", end="")
    for z in range(q, 0, -1):
        print("\t", end="")
    for w in range(n, x-1, -1):
        print(str(w)+"\t", end="")
    q += 2
    print()