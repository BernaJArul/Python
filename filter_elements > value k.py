# Python program where from a list, filter all elements greater than a given value 'k'

# Function
def new_list(list1):
   list2 = [x for x in list1 if x >= n]
   return list2

# Main Routine
original_list = [11,45,78,23,99,39]
n = int(input("Enter the value:"))
print("New list:",new_list(original_list))
