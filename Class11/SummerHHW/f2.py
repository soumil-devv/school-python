# To find sale price of an item with given cost and discount(%).

retailprice=int(input("Enter original cost:"))

discount=int(input("Enter Discount Percentage:"))

sp= round(retailprice*(1-discount/100),0)

print(f"The sale price is {sp}.")