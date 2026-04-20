#Python program to assign exception object to a variable

a = input("Enter two elements:").split()
try:
   total = int(a[0])+int(a[1])
except(ValueError,TypeError)as e:
   print("Error",e)
except IndexError:
   print("Index out of range")
finally:
   print("End of the program")
