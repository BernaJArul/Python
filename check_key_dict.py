# Python program to determine whether the key is in the dictionary

def checkKey(dic, key):
   if key in dic.keys():
      print("Present, ", end =" ")
      print("value =", dic[key])
   else:
      print("Not present")

# Main Routine
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)

key = 'w'
checkKey(dic, key)
