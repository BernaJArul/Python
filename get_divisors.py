# Python program to get the divisors of each element in the list using list comprehension

# Function
def divisor(num):
   divisors = [i for i in range(1, num + 1) if num % i == 0]
   return divisors

# Main Routine
n = int(input("Enter a number:"))
print(f"Divisors of {n}:",divisor(n))
