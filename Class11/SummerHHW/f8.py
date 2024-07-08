# WAP to read three numbers in three variables and swap first two variables with the sums of first and second ,second and third numbers, respectively.

a = int(input("Number 1="))
b = int(input("Number 2="))
c = int(input("Number 3="))

a , b = a + b , b + c

print(f"The three numbers are {a}, {b} and {c} respectively.")