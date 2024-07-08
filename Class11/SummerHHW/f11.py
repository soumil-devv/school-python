# To display the even numbers till a given limit along with their sum.

n=int((input("Limit for Numbers=")))
evenLimit = n - (n % 2)
total = 0
for c in range (evenLimit,1,-2):
    total += c
    print(c, end="   ")
print()

print(f"The sum of all even numbers to {n} is {total}.")