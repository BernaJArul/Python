#Python program to raise ZeroDivisionError if denominator is divided by 0

def divide(num, den):
   try:
      result = num / den
      return result
   except ZeroDivisionError:
      print("Error: Cannot divide by zero!")
   finally:
      print("End of the program")

num = int(input("Enter numerator:"))
den = int(input("Enter denominator:"))
result = divide(num, den)
print(result)
