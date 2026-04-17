# Python program to find the longest word in a sentence 

s = input("Enter a sentence:")

# Function to split up the words
words = s.split()

# Function to find the longest word
res = max(words, key=len)
print("The longest word is:",res)
