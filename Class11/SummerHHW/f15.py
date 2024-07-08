# To enter a number and check if it is a prime number or not.

a= int(input("Give a number:"))
a = a if a > 0 else -a

isPrime = True
for i in range(2,int(a**0.5)+1):
    if (a%i == 0) and isPrime:
        isPrime = False

if isPrime:
    print(f"{a} is a Prime Number.")
else:
    print(f"{a} is not a prime Number.")