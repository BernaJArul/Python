# Python program to calculate the length of strings and concatenate two strings

# Function 
def concat(l1,l2):
	return(len(l1),len(l2),(l1+" "+l2))

# Main routine
str1 = input("Enter 1st string:")
str2 = input("Enter 2nd string:")
x = concat(str1,str2)
print("The length of",str1,"is",x[0])
print("The length of",str2,"is",x[1])
print("Strings after concatenation:",x[2])
