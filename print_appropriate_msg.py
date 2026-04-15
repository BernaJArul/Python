# Python program to print the appropriate message

t = input("Enter a temperature:")
h = input("Enter a humidity:")
if t=='warm':
   if h=='dry':
      print("Play basketball")
   else:
      print("Play tennis")
elif t=='cold':
   if h=='dry':
      print("Play cricket")
   else:
      print("Swim")
else:
   print("None")
