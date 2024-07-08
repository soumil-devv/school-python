# To display first n natural numbers in reverse order.

x= int(input("How many numbers to display? "))

for i in range(x):
    print(x-i,end=",")
print()