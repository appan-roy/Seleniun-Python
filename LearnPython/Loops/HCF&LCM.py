""" WAP to find the HCF & LCM of two no.s. """

num1, num2 = input("Please enter two numbers : ").split()
n1 = int(num1)
n2 = int(num2)

product = n1 * n2
hcf = 0
lcm = 0

for i in range(1, product, 1):
    if n1 % i == 0 and n2 % i == 0:
        hcf = i

lcm = product / hcf

print("HCF : %d" %hcf + ", LCM : %d" %lcm)