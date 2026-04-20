# Python program to slice the list and filter odd numbers

# Function
def slice_and_filter_odd_numbers(input_list, start_index, end_index):
   # Slicing the list
   sliced_list = input_list[start_index:end_index]
   # Filtering odd numbers
   filtered_list = [num for num in sliced_list if num % 2 != 0]
   return sliced_list,filtered_list

# Main Routine
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
start_index = 0
end_index = 10
result = slice_and_filter_odd_numbers(input_list, start_index, end_index)
print("Sliced list:",result[0])
print("Filtered odd numbers from sliced list:", result[1])
