# Function to remove duplicates from a list without using lops and conditional checks
def remove_duplicates(nums):
   unique_nums = list(set(nums))
   return unique_nums

# Main Routine
num_list = [1,2,2,3,4,4,5,5,5,6]
unique_list = remove_duplicates(num_list)
print(f"List after removing duplicates:{unique_list}")
