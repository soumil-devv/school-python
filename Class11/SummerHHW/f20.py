# To accept a year and print whether it is a leap year or not.

x= int(input("The Year:"))

if x % 100 == 0:

    if x % 400 == 0:
        print(f"The year {x} {'will be'if x> 2024 else 'was'} a leap year.")
    else:
        print(f"The year {x} {'will not be'if x> 2024 else 'was not'} a leap year.")    

elif x % 4 == 0:
     print(f"The year {x} {'will be'if x> 2024 else 'was'} a leap year.")

else:
    print(f"The year {x} {'will not be'if x> 2024 else 'was not'} a leap year.")


isLeap = True
if x % 4 != 0 : isLeap = False
if x % 100 == 0: isLeap = False
if x % 400 == 0: isLeap = True

isInFuture = True if x>2024 else False

print(f"The year {x} {'will' if isInFuture else 'was'} {'' if isLeap else 'not '}{'be ' if isInFuture else ''}a leap year.")