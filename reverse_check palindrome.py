# Function
def reverse(strings):
   reversed_strings = [s[::-1] for s in strings]
   palindrome_count = sum(1 for s in reversed_strings if s == s[::-1])
   return reversed_strings, palindrome_count

# Main Routine
strings = ["madam", "hello", "racecar", "world", "level"]
result = reverse(strings)
print("Original Strins:",strings)
print("Reversed Strings:", result[0])
print("Number of Palindromes:", result[1])
