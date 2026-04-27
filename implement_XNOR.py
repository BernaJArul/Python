# Python program to implement the XNOR gate using basic gates AND, OR and NOT

def XNOR(A,B):
   res = not((A and not B) or (not A and B))
   return res

A = int(input("Enter 1st binary digit:"))
B = int(input("Enter 2nd binary digit:"))
print("The result of XNOR gate using AND, OR and NOT gate is:",XNOR(A,B))
