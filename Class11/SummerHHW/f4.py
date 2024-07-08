# To calculate Simple and Compound interest.

m= int(input("Amount of Money="))
r= int(input("Rate of interest(Per Annum)="))
t= float(input("Time period (in Years)="))


a= input("Which type of interest to calculate? ").lower()

if a =="simple":
    s= (m*r/100)*t
    total= m+s
    
    print(f"Here, the simple interest is {s} and total amount is {total}.")

elif a=="compound":
    n= float(input("Time before interest is compounded (in months)="))
    x = (t*12/n)
    print(x)
    total = m * ((1 + r/(100*x))**(x*t))
    c = total - m

    print(f"Here, the compound interest is {c} and total amount is {total}.")

else:
    print("Give a valid type of interest to calculate (Simple or Compound).")