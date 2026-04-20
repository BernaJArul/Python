def combine(odd_nums,even_nums):
   combined_list = [num for num in odd_nums] + [num for num in even_nums]
   return combined_list

# Main Routine
odd_numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8,10]
print("The appended list is:",combine(odd_numbers,even_numbers))
