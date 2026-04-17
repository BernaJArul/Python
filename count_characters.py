# python program to count the no. of characters in a string

# Function to count the no. of characters
def frequency(s):
   freq={}
   for char in s:
      if char in freq:
        freq[char]+=1
      else:
        freq[char]=1
   return freq

# Main Function
s1 = input("Enter a string:")
print("The number of characters:",frequency(s1))
