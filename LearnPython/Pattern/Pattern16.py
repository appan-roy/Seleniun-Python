""" 
1	2	3	4	5	4	3	2	1	
2	3	4	5		5	4	3	2	
3	4	5				5	4	3	
4	5						5	4	
5								5	
4	5						5	4	
3	4	5				5	4	3	
2	3	4	5		5	4	3	2	
1	2	3	4	5	4	3	2	1		
 """

n = int(input("Please enter the number of terms : "))
t = 2*n-5
s = 1

for x in range(1, n+1, 1):
    if(x != 1):
        for i in range(x, n+1, 1):
            print(str(i)+"\t", end="")
        for j in range(s, 0, -1):
            print("\t", end="")
        for k in range(n, x-1, -1):
            print(str(k)+"\t", end="")
        s += 2
    else:
        for y in range(x, n+1, 1):
            print(str(y)+"\t", end="")
        for z in range(n-1, x-1, -1):
            print(str(z)+"\t", end="")
    print()

for a in range(n-1, 0, -1):
    if a != 1:
        for p in range(a, n+1, 1):
            print(str(p)+"\t", end="")
        for q in range(1, t+1, 1):
            print("\t", end="")
        for r in range(n, a-1, -1):
            print(str(r)+"\t", end="")
        t -= 2
    else:
        for b in range(a, n+1, 1):
            print(str(b)+"\t", end="")
        for c in range(n-1, a-1, -1):
            print(str(c)+"\t", end="")
    print()