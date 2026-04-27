#Python program to realize the basic logic gates

def AND(A,B):
   return (A&B)

def OR(A,B):
   return (A|B)

def NOT(A):
   return (1-A)

def NAND(A,B):
   return not(A and B)

def NOR(A,B):
   return not(A or B)

def XOR(A,B):
   res = (A and not B) or (not A and B)
   return res

def XNOR(A,B):
   res = not((A and not B) or (not A and B))
   return res

def xnor(A,B):
   return OR(AND(A,B),AND(NOT(A),NOT(B)))


A = int(input("Enter 1st binary digit:"))
B = int(input("Enter 2nd binary digit:"))

#print("AND gate :",(AND(A,B)))
#print("OR gate  :",(OR(A,B)))
#print("NOT gate :",(NOT(A,B)))
#print("NAND gate:",(NAND(A,B)))
#print("NOR gate :",(NOR(A,B)))
#print("XOR gate :",(XOR(A,B)))
#print("XNOR gate:",(XNOR(A,B)))

print(xnor(A,B))
