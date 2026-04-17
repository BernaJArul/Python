# Python program to find sum average of N numbers using variable length arguments

# Function with multiple arguments
def sumavg(*args):
   n = len(args)
   s = 0
   for i in range(n):
      s = s + args[i]
   av = s/n
   return s, av

# Main routine
total, avg = sumavg(10,20,30,40,50)
print("Sum:",total,"Average:",avg)
