# To calculate the factorial of an inputted number.

a= int(input("Give a Number:"))

m=1
for x in range(2,a+1):
    m = m * x

print(f"Factorial of this number is {m}.")