# Function to find the greatest and minimum value from list
def great_min(nums):
   if len(nums)==0:
      return 0,0
   greatest = max(nums)
   minimum = min(nums)
   return greatest,minimum

# Main Routine
num_list = [75,89,34,67,12,99]
greatest, minimum = (great_min(num_list))
print(f"Greatest number:{greatest}, Minimum number:{minimum}")
