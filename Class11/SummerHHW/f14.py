# To print Fibonacci series up to a certain limit.
limit = int(input("Number of terms=")) 
fibList = [0,1]

for i in range(limit-2): 
    lastNum = fibList[-1]
    secondLastNum = fibList[-2]
    
    fibList.append(lastNum+secondLastNum)
    
print(fibList)