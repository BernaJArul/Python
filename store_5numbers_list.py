# Python program to create a list to store 5 different nos. and add no 5 to the existing list

# Function
def modify_list(numbers):
   modified_numbers = [num +5 for num in numbers]
   return modified_numbers

# Main Routine
numbers = [1,2,3,4,5]
result = modify_list(numbers)
print("Modified result:",result)
