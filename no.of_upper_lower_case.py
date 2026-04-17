# Python program that accepts a string and calculate the no. of upper & lower case characters

# Function
def upplow(str2):
   u,l,sc = 0,0,0
   for i in str2:
     if (i.isupper()):
       u = u+1
     elif (i.islower()):
       l = l+1
     else: 
       sc = sc+1
   return u,l,sc

# Main routine
str1 = input("Enter a string:")
x = upplow(str1)
print("The number of upper case characters are:",x[0])
print("The number of lower case characters are:",x[1])
print("The number of special characters are:",x[2])
