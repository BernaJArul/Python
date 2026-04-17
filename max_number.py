# Python function to find the max of three numbers

# Function to find max of three numbers
def max(a,b,c):
   if (a>b and a>c):
      return a
   elif (b>a and b>c):
      return b
   else:
      return c


# Main routine
x = int(input("Enter a num1:"))
y = int(input("Enter a num2:"))
z = int(input("Enter a num3:"))
print("Maximum among three numbers is:",max(x,y,z))
