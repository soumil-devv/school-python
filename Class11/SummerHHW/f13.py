# To accept a number from the user and print the table of that number.

n=int(input("Give a Number:"))

for x in range(1,21):
    a=n*x
    print(f"{n:3} x {x:2} = {a:3}")