import math
def area_of_triangle(side_a,side_b):
    area = (side_a*side_b*0.5)
    return area

print("Welcome to area calculator")
response = input("Do you want to continue? yes/no")

if response == "yes":
    side_1 = input("What is side A?: ")
    side_a = float(side_1)
    print("Side A is ", (side_a))
    side_2 = input("What is side B?: ")
    side_b = float(side_2)
    print("Side B is ", (side_b))
    print("Area of triangle is", area_of_triangle(side_a,side_b))

else:
    print("See you later")
