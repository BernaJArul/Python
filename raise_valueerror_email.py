#Python program to define a function to validate email address and raise valueError

import re

def validate_email(email):
   pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
   if not re.match(pattern, email):
      raise ValueError("Invalid email format:",email1)

email1 = input("Enter:")
email2 = "invalid-email"

try:
   validate_email(email1)
   print(email1," is a valid email address")
except ValueError as e:
   print(e)

try:
   validate_email(email2)
   print(email2," is a valid email address")
except ValueError as e:
   print(e)
