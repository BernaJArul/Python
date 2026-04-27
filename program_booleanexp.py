# Program the given boolean expression

def exp_1(A,B,C):
   res = (A and (not B)) or ( (not A) and B)or C
   return res

A = int(input("Enter 1st binary digit:"))
B = int(input("Enter 2nd binary digit:"))
C = int(input("Enter 3rd binary digit:"))

print("The result of exp1 is:",exp_1(A,B,C))
