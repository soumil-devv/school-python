#. To find average and grade for given marks

Sub = int(input("Enter Number of Subjects: "))
sum = 0

for i in range(Sub):
    sum += int(input(f"Enter Marks in Subject {i+1}: "))
avg = round(sum/Sub,2)

print(f"Total marks are {sum}.")
print(f"Average Marks are {avg}.")

gradesDict = {100:"A+" ,90:"A+" , 80:"A" , 70:"B+" , 60:"B" , 50:"C+" , 40:"C" , 30:"D" , 20:"F" , 10:"F" , 0:"F"}
grade = gradesDict[10*(avg//10)]
print(grade)