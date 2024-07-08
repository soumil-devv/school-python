# Determine whether a number is a perfect number, an Armstrong number or a palindrome.

x= int(input("Give a Number: "))

factors=[]
for c in range(1,x//2+2):
    if x%c==0:
        factors.append(c)
if sum(factors)==x:
    print(f"{x} is a Perfect number.")
else:
    print(f"{x} is not a perfect number.")

digits= list(str(x))
tsum = 0
for i in digits:
    tsum += int(i)**len(digits)

print(f"{x} is {'' if tsum==x else 'not ' }an armstrong number.")

RevDigits=digits[::-1]

if digits==RevDigits:
    print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")