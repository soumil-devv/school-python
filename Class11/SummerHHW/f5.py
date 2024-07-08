# To calculate profit-loss for given Cost and Sell Price.

b=int(input("Cost Price="))
a=int(input("Selling Price="))

if a>b:
    profit= a-b

    print(f"The shopkeeper made a profit of {profit}.")

elif b>a:
    loss= b-a

    print(f"The shopkeeper made a loss of {loss}.")

else:
    print("The shopkeeper made niether profit nor loss.")