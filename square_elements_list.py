# Python program to square the elements in the list using lambda function

# Function
def square(nums):
   squared_numbers = list(map(lambda x: x ** 2, numbers))
   return squared_numbers

# Main Routine
numbers = [1,2,3,4,5,6,7,8,9,10]
print("The squared numbers are:",square(numbers))
