""" A shopkeeper offers 30% discount on purchasing articles whereas the other shopkeeper offers two successive 
discount 20% & 10% for purchasing the same articles. WAP to compute and display which is better offer for a 
customer. """

strMP = input("Please enter thye marked price : ")
marked_price = float(strMP)

sell_price1 = marked_price * (1 - (30/100))
sell_price2 = marked_price * (1 - (20/100)) * (1 - (10/100))

if sell_price1 < sell_price2:
    print("First offer is better")
elif sell_price1 > sell_price2:
    print("Second offer is better")
else:
    print("Both offer are same")