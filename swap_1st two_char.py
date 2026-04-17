# Python program to get a single string from 2 given strings and swap 1st two characters 

# Fuction to swap first two characters
def swap(s1,s2):
   swap_s1 = s2[:2]+s1[2:]
   swap_s2 = s1[:2]+s2[2:]
   return swap_s1 +" "+ swap_s2

# Main routine
str1 = input("Enter 1st string:")
str2 = input("Enter 2nd string:")
print("After swapping fist two characters:",swap(str1,str2))
