# Python program to calculate simple_interest and compound_interest
p = int(input("Enter the value of p:"))
n  = int(input("Enter the value of n:"))  
r = int(input("Enter the value of r:"))  
t = int(input("Enter the value of t:"))
S_I = (p*n*r)/100
C_I = p* pow((1+(r/n)),(n*t))
print("SI and CI are:",S_I,C_I)
