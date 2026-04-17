# Python function to swap two numbers

# Function to swap two numbers
def swap(a,b):
   temp = a
   a = b
   b = temp
   return a,b

# Main routine
x = int(input("Enter a num1:"))
y = int(input("Enter a num2:"))
print("After swaping:", swap(x,y))
