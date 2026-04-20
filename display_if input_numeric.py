#Python program to enter a number and display the number if the input is numeric value

try:
   a = int(input("Enter the element:"))
   print(a)
except ValueError as e:
   print(e)
finally:
   print("End of the program")
