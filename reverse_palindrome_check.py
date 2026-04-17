# Python program to reverse a string and check if the string is a palindrome

# Function
def reverse(s1):
   s2 = s1[::-1]
   return s2
def palindrome(s1,s2):
   if (s1 == s2):
      return 1
   else:
      return 0
  
# Main Routine
s = input("Enter a string:") 
x = reverse(s)
print("The reverse of the string is:",x)
y = palindrome(s,x)
if y==1:
   print("The given string is a palindrome")
else:
   print("The given number is not a palindrome")
