# Python program for a simple calculator

# Function for a simple calculator
def add(num1,num2):
   return num1 + num2
def sub(num1,num2):
   return num1 - num2
def mul(num1,num2):
   return num1 * num2
def div(num1,num2):
   return num1 / num2

# Main routine
print("Operations:\n\
      1.Add\n\
      2.Subract\n\
      3.Multiply\n\
      4.Divide\n")
choice = int(input("Select operation: 1,2,3,4:"))
num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))

if choice==1:
   print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice==2:
   print(num_1,"-",num_2,"=",sub(num_1,num_2))
elif choice==3:
   print(num_1,"*",num_2,"=",mul(num_1,num_2))
else:
   print(num_1,"/",num_2,"=",div(num_1,num_2))
