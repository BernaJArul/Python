#Python program to raise an ValueError if the age of the person is negative

def set(age):
   if age < 0:
      raise ValueError("Age cannot be negative")
      print(f"Age set to{age}")
age = int(input("Enter the age:"))
try:
   set(age)
except ValueError as e:
   print(e)
finally:
   print("End of the program")
