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
