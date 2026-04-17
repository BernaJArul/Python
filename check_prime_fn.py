# Python program to returns 1 if its argument is a prime number & 0 otherwise

# Funtion
def is_prime(num):
   if num <= 1:
    return 0
   for i in range(2,int(n*0.5)+1):
     if num % i == 0:
       return 0
   return 1


# Main routine
n = int(input("Enter a number:"))
print("Answer:",is_prime(n))
