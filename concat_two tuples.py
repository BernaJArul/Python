# Python program to concatenate two tuples and print the resulting tuple

def new_list(t1,t2):
   new_list = t1 + t2
   return new_list

# Main Routine
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)
print("The new list is:",new_list(t1,t2))
