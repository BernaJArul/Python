# Python program to find lcm of two numbers
import math
n1 = int(input("Enter first num:"))
n2 = int(input("Enter second num:"))
lcm = (n1*n2)//math.gcd(n1,n2)
print("LCM is:",lcm)
