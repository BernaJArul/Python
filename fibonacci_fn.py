# Python recursive fuctuion to print the fibonacci series

# Function to print fibonacci series
def fibo(n):
   if (n==1):
      return 0
   elif (n==2):
      return 1
   else:
      return (fibo(n-1)+fibo(n-2))

# Main routine
num = int(input("Enter a number:"))
print("Fibonacci series of",num,"is:")
for i in range(1,num+1):
   fib = fibo(i)
   print(fib,end=" ")
