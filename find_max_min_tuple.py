# Python program to find max and min values from a numeric tuple

def max_min(x):
   y = max(x)
   z = min(x)
   return y,z

# Main Routine
t1 = tuple(i for i in range(1,11))
res = max_min(t1)
print("The maximun and minimum vlues are:",res[0],res[1])
