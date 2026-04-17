# Python program to sort the words in a sentence alphabetically

s = input("Enter a sentence:")

# Function to split up the words
words = s.split()

# Function to sort the gn words
words.sort()
for i in words:
   print(i, end = ' ')
