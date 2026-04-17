# Function to find the sum and average of all elements
def sum_avg(nums):
   if len(nums)==0:
      return 0,0
   tot_sum = sum(nums)
   avg = tot_sum/len(nums)
   return tot_sum, avg

# Main Routine
num_list = [86,80,88,94,98,96]
print("Result is:",sum_avg(num_list))
