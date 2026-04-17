# Function to compute the power of two numbers

# Function
def power(base,exp):
   if(exp==0):
      return 1
   elif(exp==1):
      return base
   else:
      return (base*power(base,exp-1))

# Main
a = int(input("Enter the base:"))
b = int(input("Enter the exponent:"))
res = power(a,b)
print(a,"power",b,"is:",power(a,b))
