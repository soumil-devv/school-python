# To calculate perimeter/circumference and area of shapes such as triangle, rectangle, square and circle.

from math import pi

x=input("Which shape to find area and perimeter of?").lower()

if  x =="square":
    a=float(input("Side of Square="))

    perimeter=4*a
    area= a*a

    print(f"The perimeter and area of the square are {perimeter} units and {area} units² respectively.")

elif x=="rectangle":
    b=float(input("Length of Rectangle="))
    h=float(input("Breadth of Rectangle="))

    perimeter=2*(b+h)
    area=b*h

    print(f"The perimeter and area of the rectangle are {perimeter} units and {area} units² respectively.")

elif x=="triangle":
    a=float(input("Length on Side 1="))
    b=float(input("Length on Side 2="))
    c=float(input("Length on Side 3="))
    s=(a+b+c)/2

    perimeter=a+b+c
    area= (s*(s-a)*(s-b)*(s-c))**(1/2)

    print(f"The perimeter and area of the triangle are {perimeter} units and {area} units² respectively.")

elif x=="circle":
    r= float(input("Radius of Circle="))

    circumference=round(2*pi*r,2)
    area=round(pi*(r**2),2)

    print(f"The circumference and area of the triangle are {circumference} units and {area} units² respectively.")

else:
    print("please enter a valid shape from the following: Square,Rectangle,Triangle,Circle")