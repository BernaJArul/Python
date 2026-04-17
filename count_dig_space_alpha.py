# Python program to count the no. of digits, spaces and alphabets in a given string

a = input("Enter a string:")
c1 = 0
c2 = 0
for i in a:

# Function to check if the gn character is a digit or alphabet
   if(i.isdigit()):
      c1 = c1+1
   elif(i.isalpha()):
      c2 = c2+1

# Function to count the no. of characters
c3 = a.count(" ")
print("No. of digits:",c1,"\nNo. of alphabets:",c2,"\nNo. of spaces:",c3)
