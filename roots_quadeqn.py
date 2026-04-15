# Python program to find roots of quadratic equation
import math
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = (b*b)-(4*a*c)
r1 = (-b - math.sqrt(d))/(2*a)
r2 = (-b + math.sqrt(d))/(2*a)
print("The roots are:",r1,r2)
