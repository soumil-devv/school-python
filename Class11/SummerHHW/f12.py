# To read two numbers and an arithmetic operator and displays the results.

a= float(input("Number 1= "))
b= float(input("Number 2= "))

c= input("Arithmetic Operator")

if c=="+":
    d=a+b

    print(f"Adding {a} and {b} gives {d}.")

elif c=="-":
    d=a-b

    print(f"Subtracting {b} from {a} gives {d}.")

elif c=="*":
    d=a*b

    print(f"Multiplying {a} and {b} gives {d}.")

elif c=="/":
    d=round(a/b,3)

    print(f"Dividing {b} from {a} gives {d}.")

elif c=="**":
    d=a**b

    print(f"{a} Raised to the power {b} gives {d}.")

elif c=="%":
    d=a%b

    print(f"Remainder when dividing {b} from {a} gives {d}.")