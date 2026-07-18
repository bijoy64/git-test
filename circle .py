import math


def calculate_area(radius):
    myarea = math.pi*radius**2
    return myarea
radius = calculate_area(int(input("Enter the radius of the circle: ")))
print(f"The area of the circle is: {radius}")