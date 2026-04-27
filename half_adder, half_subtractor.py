# Python program the HaldAdder and HalfSubtractor circuit

def half_adder(A,B):
   Sum = A^B
   Carry = A&B
   return Sum,Carry

def half_subtractor(A,B):
   Diff = A^B
   Borrow = (1-A)&B
   return Diff,Borrow

A = int(input("Enter 1st binary digit:"))
B = int(input("Enter 2nd binary digit:"))

print("Half_adder result is:",half_adder(A,B))
print("Half_subtractor result is:",half_subtractor(A,B))
