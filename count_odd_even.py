# Function to count the no. of odd and even numbers
def count_even_odd(nums):
   even_count=0
   odd_count=0
   for num in nums:
     if num%2==0:
       even_count+=1
     else:
       odd_count+=1
   return even_count, odd_count

# Main Routine
num_list = [1,2,3,4,5,6,7,8,9]
even_count,odd_count = count_even_odd(num_list)
print(f"Even numbers:{even_count}, Odd numbers:{odd_count}")
