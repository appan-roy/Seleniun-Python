""" WAP to check whether two no.s are co-prime or not. 
In number theory, two integers a and b are said to be relatively prime, mutually prime, 
or coprime (also written co-prime) if the only positive integer (factor) that divides both of them is 1. """

num1, num2 = input("Please enter two numbers : ").split()
n1 = int(num1)
n2 = int(num2)

maxNum = n1 if n1 > n2 else n2      # ternary --> [on_true] if [expression] else [on_false]
flag = 0

for i in range(2, maxNum, 1):
    if n1 % i == 0 and n2 % i == 0:
        flag = 1

if flag == 0:
    print("The numbers are co-prime")
else:
    print("The numbers are not co-prime")