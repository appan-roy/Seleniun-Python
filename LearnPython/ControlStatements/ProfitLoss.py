""" WAP to accept the cost price & the selling price of an article and calculate either profit
percent or loss percent. """

cost_price, sell_price = input("Please enter cost price and sell price of the item : ").split()
CP = float(cost_price)
SP = float(sell_price)

if SP > CP:
    print("Profit occured in this trade")
    profit = SP - CP
    print("The profit is : Rs. %d" %profit)
    profit_percent = (profit * 100) / CP
    print("The profit percent is : %.2f" %profit_percent + "%")
elif SP < CP:
    print("Loss occured in this trade")
    loss = CP - SP
    print("The loss is : Rs. %d" %loss)
    loss_percent = (loss * 100) / CP
    print("The loss percent is : %.2f" %loss_percent + "%")
else:
    print("No profit no loss occured in this trade")