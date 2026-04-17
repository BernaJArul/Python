# Function to find the second largest number in the list
def second_largest(numbers):
   first = 0
   second = 0
   for n in numbers:
     if n > first:
       first, second = n,first
     elif first > n > second:
       second = n
   return second or 0

# Main Routine
num_list=[2,9,7,5,4,3]
print(second_largest(num_list))
