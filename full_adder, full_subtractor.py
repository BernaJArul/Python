# Python program the FullAdder and FullSubtractor circuit

def full_adder(A,B,C):
   Sum = (A^B)^C
   Carry = ( C & (A^B) ) | A & B
   return Sum,Carry

def full_subtractor(A,B,C):
   Diff = (A^B)^C
   Borrow = (1-A) & B | (1-A) & C | B & C
   return Diff,Borrow

A = int(input("Enter 1st binary digit:"))
B = int(input("Enter 2nd binary digit:"))
C = int(input("Enter 3rd binary digit:"))

print("Full_adder result is:",full_adder(A,B,C))
print("Full_subtractor result is:",full_subtractor(A,B,C))
