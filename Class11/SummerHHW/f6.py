# To convert the time given in minutes into hours and minutes.

a= int(input("Time(in minutes):"))

b= a // 60
c= a % 60

print(f"The time is {b} hours and {c} minutes.")