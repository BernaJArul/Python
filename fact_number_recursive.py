# Python recursive function to calculate the factorial of a number

# Function to find the factorial of a number
def fact(n):
   if (n==0):
      return 1
   else:
      return (n*fact(n-1))

# Main routine
num = int(input("Enter a number:"))
print("Factorial of",num,"is",fact(num))
[24bec004@mepcolinux ex3]$cat 3.py
# Python function to swap two numbers

# Function to swap two numbers
def swap(a,b):
   temp = a
   a = b
   b = temp
   return a,b
