# Python program to unpack a tuple of four elements into four variables

def variable(tuple2):
   a,b,c,d = tuple2
   return a,b,c,d

# Main Routine
tuple1 = ('Berna J Arul','ECE_A','24BEC04','03/06/2006')
x = variable(tuple1)
print("Name:",x[0],"\nClass:",x[1],"\nRoll.No:",x[2],"\nD/O/B:",x[3])
