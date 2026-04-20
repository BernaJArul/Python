#Python Program to raise a RuntimeError if radius of circle is negative

def set(radius):
   if radius < 0:
      raise RuntimeError("Radius of the circle cannot be negative")
   print(f"Radius set to {radius}")
radius = int(input("Enter the radius:"))
try:
   set(radius)
except RuntimeError as e:
   print(e)
finally:
   print("End of the program")
