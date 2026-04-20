# Python program to find the repeated items of a tuple

def repeated(tup):
   x = {item for item in tup if tup.count(item)>1}
   return x

tup = (1,1,1,2,3,4,7,8,5,5,4)
print("The duplicates are:",repeated(tup))
