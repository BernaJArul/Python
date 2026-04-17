# Function to count the number of vowels in a string

# Function to count the number of vowels
def vow_count(string):
   vowels = "aeiouAEIOU"
   count = sum(1 for char in string if char in vowels)
   return count
   

# Main routine
text = input("Enter a string:")
print("The number of vowels in",text,"is:",vow_count(text))
