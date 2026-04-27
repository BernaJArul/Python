#Python program to calculate the area of circle using math module

import math

def circle_area(radius):
   result = math.pi * radius**2
   return result

radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print("The area of the circle is:", area)
