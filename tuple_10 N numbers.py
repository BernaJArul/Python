# Python program to create a tuple of 1st 10 natural numbers

def square():
   x = tuple(i**2 for i in range(1,11))
   return x

# Main Routine
print(square())
